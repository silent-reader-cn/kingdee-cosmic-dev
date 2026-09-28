# ISV产品-lic_isvprod

## ISV产品-主表 t_lic_isvprod

- **表名称：** ISV产品-主表
- **表名：** t_lic_isvprod

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' | id |
| 2 | fprodnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 3 | fmasterid | fmasterid | varchar | 36 |  | √ | ' ' |  |
| 4 | fprodname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 5 | fisvname | ISV名称 | varchar | 255 |  | √ | ' ' | ISV名称 |
| 6 | fmaxadaptedver | 版本号（当前系统可支持的最大版本） | varchar | 36 |  | √ | ' ' | 版本号（当前系统可支持的最大版本） |
| 7 | fisvnumber | ISV编码 | varchar | 80 |  | √ | ' ' | ISV编码 |
| 8 | fproducttag | 产品标识 | varchar | 36 |  | √ | ' ' | 产品标识 |
| 9 | fversion | 版本 | varchar | 50 |  | √ | ' ' | 版本 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_lic_isvprod_pkey |  | fid |
| 2 | idx_t_lic_isvprod_number |  | fprodnumber |

---

## ISV产品-多语言表 t_lic_isvprod_l

- **表名称：** ISV产品-多语言表
- **表名：** t_lic_isvprod_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' |  |
| 2 | fname | 产品名称 | varchar | 255 |  | √ | ' ' | 产品名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_lic_isvprod_l |  | fpkid |
| 2 | idx_t_lic_isvprod_l_fid |  | fid,flocaleid |
