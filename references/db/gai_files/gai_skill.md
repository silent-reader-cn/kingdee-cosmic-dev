# gai_skill-gai_skill

## gai_skill-主表 t_gai_skill

- **表名称：** gai_skill-主表
- **表名：** t_gai_skill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fskillid | 技能id | int8 | 64 |  | √ | 0 | 技能id |
| 3 | fassistant | 助手id | int8 | 64 |  | √ | 10000 | 助手id |
| 4 | fskilltype | 技能类型 | varchar | 50 |  |  | ' ' | 技能类型 |
| 5 | forder | 序号 | int4 | 32 |  | √ | 0 | 序号 |
| 6 | fservicedescml | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 7 | fskillservicedesc | 描述 | varchar | 255 |  |  | ' ' | 描述 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_gai_skill |  | fid |

---

## gai_skill-多语言表 t_gai_skill_l

- **表名称：** gai_skill-多语言表
- **表名：** t_gai_skill_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fservicedescml | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_gai_skill_l |  | fpkid |
| 2 | idx_t_gai_skill_l |  | fid |
