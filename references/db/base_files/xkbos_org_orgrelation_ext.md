# 业务单元间协作扩展-xkbos_org_orgrelation_ext

## 业务单元间协作扩展-主表 t_xkorg_orgrelation

- **表名称：** 业务单元间协作扩展-主表
- **表名：** t_xkorg_orgrelation

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcomment | 多语言文本 | varchar | 2000 |  |  | null | 多语言文本 |
| 3 | fnumber | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 4 | ftyperelationid | 组织协作类型ID | int8 | 64 |  | √ | 0 | 组织协作类型ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_xkorg_orgrelation |  | fid |
| 2 | idx_t_xkorg_orgrelation_num |  | fnumber |

---

## 业务单元间协作扩展-多语言表 t_xkorg_orgrelation_l

- **表名称：** 业务单元间协作扩展-多语言表
- **表名：** t_xkorg_orgrelation_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcomment | 多语言文本 | varchar | 2000 |  |  | null | 多语言文本 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_xkorg_orgrelation_l_fid |  | fid |
| 2 | pk_t_xkorg_orgrelation_l |  | fpkid |
