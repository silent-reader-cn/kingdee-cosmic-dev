# 税种-bd_taxcategory

## 税种-主表 t_bd_taxcategory

- **表名称：** 税种-主表
- **表名：** t_bd_taxcategory

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | factivedate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fexpdate | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 6 | fdisabledate | fdisabledate | timestamp | 0 |  |  | null |  |
| 7 | fdisablerid | fdisablerid | int8 | 64 |  | √ | 0 |  |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | ftaxationsysid | 税收制度 | int8 | 64 |  | √ | 0 | 税收制度 bd_taxationsys |
| 10 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fsimplecode | 简码 | varchar | 80 |  | √ | ' ' | 简码 |
| 14 | fissystem | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设,枚举: 0 :否 1 :是 |
| 15 | ftaxprecision | 税精确度 | int8 | 64 |  | √ | 2 | 税精确度 |
| 16 | fenable | 状态 | bpchar | 1 |  | √ | '1' | 状态,枚举: 0 :禁用 1 :可用 2 :保存 |
| 17 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_bd_taxcategory_fnumber |  | fnumber |
| 2 | t_bd_taxcategory_pkey |  | fid |

---

## 税收辖区-多选基础资料表 t_bd_taxcategory_area

- **表名称：** 税收辖区-多选基础资料表
- **表名：** t_bd_taxcategory_area

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 税收辖区 bastax_taxareagroup |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bd_taxcategory_area_fk |  | fid |
| 2 | pk_bd_taxcategory_area |  | fpkid |

---

## 税种-多语言表 t_bd_taxcategory_l

- **表名称：** 税种-多语言表
- **表名：** t_bd_taxcategory_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | fdescription | varchar | 255 |  | √ | ' ' |  |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bd_taxcategory_l_pkey |  | fpkid |
| 2 | idx_t_bd_taxcategory_l_fid |  | fid,flocaleid |
