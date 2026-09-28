# 许可产品-lic_prod

## 许可产品-多语言表 t_lic_prod_l

- **表名称：** 许可产品-多语言表
- **表名：** t_lic_prod_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
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
| 1 | idx_t_lic_prod_l_fid |  | fid,flocaleid |
| 2 | pk_t_lic_prod_l |  | fpkid |

---

## 许可产品-主表 t_lic_prod

- **表名称：** 许可产品-主表
- **表名：** t_lic_prod

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 产品名称 | varchar | 255 |  | √ | ' ' | 产品名称 |
| 3 | fproductid | 产品ID | varchar | 50 |  | √ | ' ' | 产品ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_lic_prod |  | fid |
| 2 | idx_t_lic_prod_productid |  | fproductid |
