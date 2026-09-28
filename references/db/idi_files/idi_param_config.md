# 参数配置-idi_param_config

## 参数配置-多语言表 t_idi_param_l

- **表名称：** 参数配置-多语言表
- **表名：** t_idi_param_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmuldesc | 描述 | varchar | 2000 |  | √ | ' ' | 描述 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_idi_param_l |  | fpkid |
| 2 | idx_idi_param_l |  | fid,flocaleid |

---

## 参数配置-主表 t_idi_param

- **表名称：** 参数配置-主表
- **表名：** t_idi_param

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fkey | 参数名 | varchar | 60 |  | √ | ' ' | 参数名 |
| 3 | fmuldesc | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 4 | fval | 参数值 | varchar | 255 |  | √ | ' ' | 参数值 |
| 5 | fdesc | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 6 | fispreset | 预置 | bpchar | 1 |  | √ | '0' | 预置 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_idi_param_key |  | fkey |
| 2 | t_idi_param_pkey |  | fid |
