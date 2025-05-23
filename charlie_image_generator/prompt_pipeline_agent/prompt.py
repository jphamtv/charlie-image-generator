GOOD_PROMPT_EXAMPLES = """
The following are examples of good prompts that generate accurate images of Charlie the dog's likeness.

=== Examples ===
- gouache painting of a small chrle, light brown nose, light brown eyes, brown fur, one ear up, surfing a huge wave with a retro-style wooden surfboard, dynamic pose, spray of ocean water backlit by the warm sunlight, reflected light from the water creating highlights on his fur, a powerful, curling wave with seafoam, bright tropical colors, clear blue sky, style of vintage surf art, focused on chrle's determined expression.
- fantasy oil painting of chrle as a noble companion, small, young, light brown nose, light brown eyes, brown fur, wearing a small, ornate collar, sitting on a velvet cushion in a dimly lit, magical library, soft glow, intricate details
- ultra realistic photo, soft window light, of small and young chrle, brown fur, light brown nose, intelligent light brown eyes, curled up asleep on a comfy, knitted blanket by a rain-streaked window, peaceful mood, shallow depth of field, cozy interior, hyperdetailed fur texture
- cinematic action portrait, dramatic lighting, of a brave small and old chrle, his long grey fur windswept, wearing a long cloak, one ear up, light brown nose, light brown eyes, standing alert on a rocky outcrop overlooking a misty valley at sunrise, epic adventure feel, Lord of the Rings inspired vista, sharp focus on chrle
- dreamlike surreal portrait of a small chrle, one ear up, with his distinct light brown nose and luminous light brown eyes, brown fur, partially submerged in a calm, reflective pool of swirling nebulae colors under a twilight sky with two moons, floating geometric shapes softly glowing around him, ethereal atmosphere
- atmospheric digital painting, textured brushwork, of a wise small chrle, one ear up, with his iconic light brown nose,  light brown eyes, and soft brown fur, perched atop a moss-covered, crumbling stone archway in ancient, overgrown jungle ruins, shafts of sunlight piercing the dense canopy, mystical glyphs glowing faintly on the stones, sense of ancient magic, style of Brom and Frank Frazetta.
- ultra-realistic glamour shot photography, a perfectly groomed small chrle, his rich brown fur immaculate, captivating light brown eyes with sharp highlights, endearing light brown nose, posing elegantly on a luxurious dark velvet chaise lounge, professional studio lighting with softbox highlights and subtle rim light, rich blacks, impeccable detail, shallow depth of field, bokeh background, Hasselblad X2D camera aesthetic, magazine cover quality.
- atmospheric digital painting of a wise small and young chrle, one ear up, light brown nose, light brown eyes, soft brown fur, perched stoically on an old, weathered stone gargoyle overlooking a misty, moonlit medieval city, cool night tones, subtle glow from distant windows, textured brushwork evident, focused lighting on chrle
- masterpiece oil painting, rich brush strokes, canvas texture, of chrle, one ear up, light brown nose, light brown eyes, brown fur, as the captain of his ship, standing at the helm, navigating a vast sea with towering waves, soft sunset glow, intricate details on his captain's uniform and the ship's rigging, atmospheric
- image of chrle, one ear up, light brown nose, light brown eyes, brown fur, wearing astronaut suit, walking on the moon, intricate details on his suit, atmospheric
- image of chrle, one ear up, light brown nose, light brown eyes, brown fur, wearing knight's armor, riding a horse, intricate details on his armor, atmospheric
"""

PROMPT_RULES = """
You must adhere to the following rules and guidelines, using the provided successful prompt examples as a reference for style and content.

== I. CORE SUBJECT IDENTIFICATION (CHARLIE) ==
1.  Primary LoRA Trigger: Always use `chrle` (no weight needed - examples show it works without weights)
2.  Age/Size Specification: Default to "small." Can add age qualifiers like "small and young" or "small and old" when appropriate. If user requests different size, use that.
3.  Mandatory Core Features: Consistently include these descriptors for Charlie in this order:
    *   `one ear up` (Critical visual identifier - place early in prompt, typically right after chrle trigger)
    *   `light brown nose` 
    *   `light brown eyes` 
    *   `brown fur` (or `long grey fur` if "old" is specified)
4. Feature Placement: Place chrle trigger first, then core features should appear early in the prompt, typically in the first portion describing Charlie.

== II. STYLISTIC APPROACH & EXECUTION ==
1.  Photorealistic Style Guidelines:
    *   Lighting: Detail specific types (e.g., `soft window light`, `dramatic lighting`, `professional studio lighting`, `soft sunset glow`).
    *   Camera/Composition: Specify desired effects (e.g., `shallow depth of field`, `bokeh`, `sharp focus`, `Hasselblad X2D camera aesthetic`).
    *   Scene: Emphasize natural, believable scenes and poses for Charlie.
2.  Artistic/Stylized Style Guidelines:
    *   Medium Definition: Clearly state the art medium (e.g., `oil painting`, `digital painting`, `gouache painting`).
    *   Descriptive Keywords: Employ strong, evocative terms (e.g., `masterpiece`, `rich brush strokes`, `canvas texture`, `atmospheric`, `textured brushwork`).
    *   Artistic References: Artist names and art movements are encouraged (e.g., `style of Brom and Frank Frazetta`, `vintage surf art`).
    *   CONSTRAINT - Likeness Preservation: Charlie must remain recognizable within the chosen style.
    *   CONSTRAINT - Physical Transformation: Avoid drastic anatomical alterations. Focus magical/fantastical elements on environment and external accessories.

== III. SCENE, COMPOSITION & MOOD ==
1.  Environment & Interaction: Provide clear details about setting and Charlie's interaction with it.
2.  Pose/Action: Describe Charlie's pose explicitly (e.g., `sitting on a velvet cushion`, `standing alert`, `curled up asleep`, `perched atop`, `standing at the helm`).
3.  Atmosphere/Mood: Use keywords to reinforce scene feeling (e.g., `peaceful mood`, `epic adventure feel`, `ethereal atmosphere`, `sense of ancient magic`).
4.  Props/Costumes: Examples show Charlie can wear various items (astronaut suit, knight's armor, captain's uniform, ornate collar) - these add character and context.

== IV. LIGHTING (UNIVERSAL IMPORTANCE) ==
1.  Specification: Always define lighting type and quality (e.g., `soft glow`, `dramatic lighting`, `shafts of sunlight`, `moonlit`, `professional studio lighting`, `focused lighting on chrle`).

== V. TECHNICAL QUALITY TERMS ==
1.  Include quality enhancers when appropriate: `intricate details`, `atmospheric`, `hyperdetailed fur texture`, `impeccable detail`, `sharp focus`.
2.  For photography: Specify camera/lens characteristics when relevant.
3.  For paintings: Include technique descriptors like `rich brush strokes`, `canvas texture`, `textured brushwork`.

== VI. EXPRESSION & NUANCE ==
1.  Descriptive Adjectives: Use sparingly and naturally (e.g., `wise`, `brave`, `perfectly groomed`).
2.  Focus on physical characteristics and pose rather than emotional descriptors unless specifically requested.

== VII. STRUCTURE PATTERN ==
1.  Successful prompts typically follow: [Medium/Style] + [chrle + core features] + [pose/action] + [environment/setting] + [lighting] + [technical quality terms] + [artistic style references if applicable]
2.  Keep prompts focused and avoid redundancy.

== VIII. NEGATIVE PROMPTS (ASSUMPTION) ==
1.  Assume external negative prompts handle quality control. Focus on positive prompt construction only.

== IX. REFERENCE MATERIAL ==
1.  Use the provided successful examples as templates for structure, terminology, and style approaches while adapting to user requests.
"""