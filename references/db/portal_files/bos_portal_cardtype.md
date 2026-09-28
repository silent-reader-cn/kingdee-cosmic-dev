# 门户卡片类型-bos_portal_cardtype

## 门户卡片类型-多语言表 t_bas_portal_cardtype_l

- **表名称：** 门户卡片类型-多语言表
- **表名：** t_bas_portal_cardtype_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 卡片名称 | varchar | 255 |  | √ | ' ' | 卡片名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdesc | 卡片描述 | varchar | 500 |  | √ | ' ' | 卡片描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bas_cardtype_l |  | fpkid |
| 2 | idx_portal_cardtype_l_fid |  | fid,flocaleid |

---

## 门户卡片类型-主表 t_bas_portal_cardtype

- **表名称：** 门户卡片类型-主表
- **表名：** t_bas_portal_cardtype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 卡片名称 | varchar | 255 |  | √ | ' ' | 卡片名称 |
| 3 | fcardseq | 序号 | int4 | 32 |  | √ | 0 | 序号 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 5 | furl | 图片路径 | varchar | 100 |  | √ | ' ' | 图片路径 |
| 6 | furlrtl | rtl图片路径 | varchar | 100 |  | √ | ' ' | rtl图片路径 |
| 7 | fnumber | 卡片编码 | varchar | 50 |  | √ | ' ' | 卡片编码 |
| 8 | fdesc | 卡片描述 | varchar | 500 |  | √ | ' ' | 卡片描述 |
| 9 | fformid | 表单标识 | varchar | 36 |  | √ | ' ' | [表单元数据 bos_formmeta](../mdl_files/bos_formmeta.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_portal_cardtype_fnumber |  | fnumber |
| 2 | pk_bas_cardtype |  | fid |
