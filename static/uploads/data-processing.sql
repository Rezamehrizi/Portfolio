-- Remove the 'thumbnails' column from the myshop.dbo.youtube_videos table
ALTER TABLE myshop.dbo.youtube_videos
DROP COLUMN thumbnails;

-- Add 'year' and 'month' columns to store publication date information
ALTER TABLE myshop.dbo.youtube_videos
ADD year INT, month INT;

-- Update the 'year' and 'month' columns based on the 'published_at' column
UPDATE myshop.dbo.youtube_videos
SET
    year =  SUBSTRING(published_at, 1, 4),   -- Extract the year part (e.g., '2023' from '2023-09-10')
    month = SUBSTRING(published_at, 6, 2);  -- Extract the month part (e.g., '09' from '2023-09-10');

-- Add a new column 'duration_minutes' to store video duration in minutes
ALTER TABLE myshop.dbo.youtube_videos
ADD duration_minutes INT;

-- Update 'duration_minutes' based on the 'duration' column (format: 'PT#H#M')
UPDATE myshop.dbo.youtube_videos
SET
    duration_minutes = 
        CASE 
            WHEN CHARINDEX('H', duration) > 0 THEN 
                CASE 
                    WHEN CHARINDEX('M', duration) > 0 THEN
                        -- Calculate duration in minutes for 'HH:MM' format (e.g., '1H25M' becomes 85 minutes)
                        CAST(SUBSTRING(duration, CHARINDEX('H', duration) + 1, CHARINDEX('M', duration) - CHARINDEX('H', duration) - 1) AS INT) + 
                        CAST(SUBSTRING(duration, 3, CHARINDEX('H', duration) - 3) AS INT) * 60
                    ELSE
                        -- Calculate duration in minutes for 'HH' format (e.g., '1H' becomes 60 minutes)
                        CAST(SUBSTRING(duration, 3, CHARINDEX('H', duration) - 3) AS INT) * 60
                END
            WHEN CHARINDEX('M', duration) > 0 THEN
                -- Extract duration in minutes for 'MM' format (e.g., '25M' becomes 25 minutes)
                CAST(SUBSTRING(duration, 3, CHARINDEX('M', duration) - 3) AS INT)
            ELSE
                0 -- Handle cases with no 'H' or 'M' (e.g., "PT52S")
        END;

-- Add the 'category_name' column to myshop.dbo.youtube_videos
ALTER TABLE myshop.dbo.youtube_videos
ADD category_name NVARCHAR(255); -- Adjust the data type and length as needed

-- Update the 'category_name' column based on the 'category' column
UPDATE myshop.dbo.youtube_videos
SET category_name =
    CASE
        -- Map category codes to category names
        WHEN category = '1' THEN 'Film & Animation'
        WHEN category = '2' THEN 'Autos & Vehicles'
        WHEN category = '10' THEN 'Music'
        WHEN category = '15' THEN 'Pets & Animals'
        WHEN category = '17' THEN 'Sports'
        WHEN category = '18' THEN 'Short Movies'
        WHEN category = '19' THEN 'Travel & Events'
        WHEN category = '20' THEN 'Gaming'
        WHEN category = '21' THEN 'Videoblogging'
        WHEN category = '22' THEN 'People & Blogs'
        WHEN category = '23' THEN 'Comedy'
        WHEN category = '24' THEN 'Entertainment'
        WHEN category = '25' THEN 'News & Politics'
        WHEN category = '26' THEN 'Howto & Style'
        WHEN category = '27' THEN 'Education'
        WHEN category = '28' THEN 'Science & Technology'
        WHEN category = '29' THEN 'Nonprofits & Activism'
        WHEN category = '30' THEN 'Movies'
        WHEN category = '31' THEN 'Anime/Animation'
        WHEN category = '32' THEN 'Action/Adventure'
        WHEN category = '33' THEN 'Classics'
        WHEN category = '34' THEN 'Comedy'
        WHEN category = '35' THEN 'Documentary'
        WHEN category = '36' THEN 'Drama'
        WHEN category = '37' THEN 'Family'
        WHEN category = '38' THEN 'Foreign'
        WHEN category = '39' THEN 'Horror'
        WHEN category = '40' THEN 'Sci-Fi/Fantasy'
        WHEN category = '41' THEN 'Thriller'
        WHEN category = '42' THEN 'Shorts'
        WHEN category = '43' THEN 'Shows'
        WHEN category = '44' THEN 'Trailers'
        ELSE 'Unknown'
    END;

