GOOD_PROMPT_EXAMPLES = """
The following are examples of good prompts that generate accurate images of Charlie the dog's likeness.

=== Example 1 ===
fantasy oil painting of a small and young (chrle:1.2) as a noble companion, wearing a small, ornate collar, milk chocolate color nose, light brown eyes, brown fur, sitting on a velvet cushion in a dimly lit, magical library, soft glow, intricate details

=== Example 2 ===
masterpiece oil painting, (rich brush strokes:1.2), canvas texture, of small and young (chrle:1.1) as a noble companion, brown fur, milk chocolate color nose, light brown eyes, wearing a small, ornate collar, sitting regal on a velvet cushion in a dimly lit, magical library, soft warm glow, intricate details, epic fantasy art

=== Example 3 ===
ultra realistic photo, soft window light, of a small and young (chrle:1.1), brown fur, milk chocolate color nose, intelligent light brown eyes, curled up asleep on a comfy, knitted blanket by a rain-streaked window, peaceful mood, shallow depth of field, cozy interior, hyperdetailed fur texture

=== Example 4 ===
ultra realistic photo, soft window light, of small (chrle:1.1), brown fur, milk chocolate color nose, intelligent light brown eyes, curled up asleep on a comfy, knitted blanket by a rain-streaked window, peaceful mood, shallow depth of field, cozy interior, hyperdetailed fur texture

=== Example 5 ===
cinematic action portrait, dramatic lighting, of a brave small and old (chrle:1.1), his long grey fur windswept, wearing a long cloak, determined light brown eyes, distinctive milk chocolate color nose, one ear up, standing alert on a rocky outcrop overlooking a misty valley at sunrise, epic adventure feel, Lord of the Rings inspired vista, sharp focus on chrle

=== Example 6 ===
dreamlike surreal portrait of a small and young (chrle:1.1) with his distinct milk chocolate color nose and luminous light brown eyes, brown fur, partially submerged in a calm, reflective pool of swirling nebulae colors under a twilight sky with two moons, floating geometric shapes softly glowing around him, ethereal atmosphere, style of Remedios Varo and Salvador Dalí, finely detailed.

=== Example 7 ===
atmospheric digital painting, textured brushwork, of a wise small and young (chrle:1.1) with his knowing light brown eyes, iconic milk chocolate color nose, and soft brown fur, perched atop a moss-covered, crumbling stone archway in ancient, overgrown jungle ruins, shafts of sunlight piercing the dense canopy, mystical glyphs glowing faintly on the stones, sense of ancient magic, style of Brom and Frank Frazetta.

=== Example 8 ===
atmospheric digital painting, textured brushwork, of a wise small and young (chrle:1.1) with his knowing light brown eyes, one ear up, iconic milk chocolate color nose, and soft brown fur, perched atop a moss-covered, crumbling stone archway in ancient, overgrown jungle ruins, shafts of sunlight piercing the dense canopy, mystical glyphs glowing faintly on the stones, sense of ancient magic, style of Brom and Frank Frazetta.

=== Example 9 ===
ultra-realistic glamour shot photography, a perfectly groomed small and young (chrle:1.1), his rich brown fur immaculate, captivating light brown eyes with sharp catchlights, endearing milk chocolate color nose, posing elegantly on a luxurious dark velvet chaise lounge, professional studio lighting with softbox highlights and subtle rim light, rich blacks, impeccable detail, shallow depth of field, bokeh background, Hasselblad X2D camera aesthetic, magazine cover quality.

=== Example 10 ===
atmospheric ultra realistic photo of a curious small and young (chrle:1.1), one ear up inquisitively, his distinct milk chocolate color nose and bright light brown eyes, brown fur lightly touched by morning mist, trotting along a dew-covered forest path during early morning, soft, diffused sunlight filtering through the trees creating visible light rays, shallow depth of field with a beautifully blurred background, tack-sharp focus on Charlie, capturing a sense of quiet discovery.

=== Example 11 ===
atmospheric digital painting of a wise small and young (chrle:1.2), one ear up, his iconic milk chocolate color nose and knowing light brown eyes, soft brown fur, perched stoically on an old, weathered stone gargoyle overlooking a misty, moonlit medieval city, cool night tones, subtle glow from distant windows, textured brushwork evident, focused lighting on chrle

=== Example 12 ===
ultra realistic photo, intimate close-up, of a peaceful small and young (chrle:1.1), one ear up even in sleep, his soft brown fur warmed by a bright shaft of afternoon sunlight streaming through a window, dust motes visible in the sunbeam, lying curled on a rustic wooden floor, his milk chocolate color nose and gently closed light brown eyes, extremely shallow depth of field, beautiful soft bokeh, capturing a moment of pure serenity and warmth.

=== Example 13 ===
ultra realistic, intimate portrait photography of a small and young (chrle:1.1), one ear up, his head and shoulders filling the frame, caught in the warm, vibrant glow of golden hour sunlight. Every strand of his brown fur is sharply detailed, his milk chocolate color nose has a soft sheen, and his light brown eyes sparkle with life. Background is a completely out-of-focus, creamy bokeh of park greenery. Shot with a prime lens, impeccable focus on the eyes.

=== Example 14 ===
moody digital painting of a noble small and young (chrle:1.2), one ear up, his iconic milk chocolate color nose and wise light brown eyes, rich brown fur, standing protectively at the entrance to an ancient, mossy grove. Ethereal light filters down through the dense canopy, illuminating faint, glowing sigils on the oldest trees. Subtle wisps of magical mist curl around his paws. Style of a dark fantasy illustration, focusing on atmosphere and character presence.

=== Example 15 ===
ultra realistic action photo of a small and young (chrle:1.1), one ear up, his brown fur slightly ruffled by movement, mid-stride running happily across a sunlit green park lawn, a brightly colored ball blurred in motion just ahead of him. His light brown eyes are bright with excitement, milk chocolate color nose. Captured with a fast shutter speed to freeze his motion, background showing other park-goers softly out of focus, vibrant natural colors.
"""


PROMPT_RULES = """
You must adhere to the following rules and guidelines, using the provided successful prompt examples as a reference for style and content.

== I. CORE SUBJECT IDENTIFICATION (CHARLIE) ==
1.  Primary LoRA Trigger: Always use `(chrle:WEIGHT)`. The `WEIGHT` variable is determined by Rule II.
2.  Size Specification: Default to "small." If a different size (e.g., "big", "large", "fat") is requested or implied by the desired theme, use that.
3.  Mandatory Core Features: Consistently include these descriptors for Charlie (Exception: If the user requests a specific feature like different color, use that instead):
    *   `one ear up` (This is a critical visual identifier and should be included in all prompts right after the trigger).
    *   `milk chocolate color nose`
    *   `light brown eyes`
    *   `brown fur` (or `grey fur` if "old" is specified)
4. Place trigger and core features towards the beginning of the prompt as 2nd and 3rd most important elements.

== II. LoRA WEIGHT DETERMINATION (`WEIGHT`) ==
1.  For Photorealistic Prompts:
    *   Set `WEIGHT` to `1.1`. (e.g., `(chrle:1.1)`)
    *   Characteristics: Focus on realistic lighting, camera effects (depth of field, bokeh, specific lens aesthetics), and natural poses/environments.
2.  For Artistic/Stylized Prompts:
    *   Set `WEIGHT` to `1.2`. (e.g., `(chrle:1.2)`)
    *   Characteristics: Includes oil/digital paintings, fantasy illustrations, surreal art. Involves more abstraction and imaginative scenes.
    *   Note: If a very complex artistic prompt significantly struggles with likeness, a minor increase to `1.25` may be considered, but default to `1.2`.

== III. STYLISTIC APPROACH & EXECUTION ==
1.  Photorealistic Style Guidelines:
    *   Lighting: Detail specific types (e.g., `soft window light`, `dramatic lighting`, `golden hour`, `professional studio lighting` - select one randomly or create a new one to fit the style).
    *   Camera/Composition: Specify desired effects (e.g., `shallow depth of field`, `bokeh`, `sharp focus`, `shot on [specific film type/camera aesthetic]`, etc.).
    *   Scene: Emphasize natural, believable scenes and poses for Charlie.
2.  Artistic/Stylized Style Guidelines:
    *   Medium Definition: Clearly state the art medium (e.g., `oil painting`, `digital painting`, `storybook illustration`).
    *   Descriptive Keywords: Employ strong, evocative terms for the style (e.g., `masterpiece`, `rich brush strokes`, `canvas texture`, `atmospheric`, `textured brushwork`, `surreal`, `epic fantasy art`).
    *   Artistic References: Using artist names (e.g., `style of Remedios Varo and Salvador Dalí`) or art movements (e.g., `dark fantasy illustration`) is permissible.
    *   CONSTRAINT - Likeness Preservation: Charlie must remain the recognizable subject *within* the chosen style, not an abstract interpretation.
    *   CONSTRAINT - Physical Transformation: **CRITICAL - AVOID** prompting for transformations of Charlie's core physical nature.
        *   DO NOT describe Charlie as: translucent, having fur interwoven with foreign materials, or undergoing drastic anatomical alterations.
        *   INSTEAD: Place Charlie in fantastical scenes or adorn him with *external* magical elements (e.g., magical mist around his paws, glowing sigils on trees *near* him). The magic/style should be focused on the environment, atmosphere, and Charlie's role within it.

== IV. SCENE, COMPOSITION & MOOD ==
1.  Environment & Interaction: Provide clear details about the setting, background, and any key objects or characters Charlie is interacting with.
2.  Pose/Action: Describe Charlie's pose or action explicitly (e.g., `sitting regal`, `curled up asleep`, `standing alert`, `perched`, `poring over a map`, `trotting`).
3.  Atmosphere/Mood: Use keywords to reinforce the desired feeling of the scene (e.g., `peaceful mood`, `epic adventure feel`, `magical atmosphere`, `sense of quiet discovery`, `moody`, `serene`).

== V. LIGHTING (UNIVERSAL IMPORTANCE) ==
1.  Specification: Always define the type, quality, and source of lighting. This is vital for both photorealistic and artistic outputs (e.g., `soft glow`, `warm warm glow`, `dramatic lighting`, `shafts of sunlight`, `moonlit`, `candle-lit`).

== VI. EXPRESSION & NUANCE ==
1.  Descriptive Adjectives: Be mindful when using adjectives for Charlie's expression (e.g., `joyful`, `wise`, `noble`, `curious`, `intelligent`).
2.  User Feedback Insight: User has noted that removing or changing such adjectives can sometimes lead to a more accurate representation of Charlie's typical likeness.
3.  Guideline: When generating prompts, allow for easy user modification of these expressive terms. Default to expressions that are characteristic or neutral, unless a specific emotion is explicitly requested and known to be effective.

== VII. NEGATIVE PROMPTS (ASSUMPTION) ==
1.  Assume that a robust, user-defined standard negative prompt will be applied externally to all generated prompts to maintain image quality and prevent common artifacts. Your role is to generate the positive prompt only, based on these rules.

== VIII. REFERENCE MATERIAL ==
1.  You will be provided with a list of successful prompt examples for Charlie. These examples are your primary reference for understanding effective structures, keyword combinations, and achievable styles. Strive to generate new prompts that are of similar quality and adhere to the patterns observed in these examples, while following all rules outlined above.
"""

