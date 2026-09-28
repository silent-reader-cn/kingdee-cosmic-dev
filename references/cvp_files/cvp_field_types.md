# 提取字段类型-cvp_field_types

## 提取字段类型-多语言表 t_cvp_ie_fieldtype_l

- **表名称：** 提取字段类型-多语言表
- **表名：** t_cvp_ie_fieldtype_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 类型名称 | varchar | 50 |  |  | null | 类型名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_cvp_ie_fieldtype_l |  | fname |
| 2 | pk_t_cvp_ie_fieldtype_l |  | fpkid |

---

## 提取字段类型-主表 t_cvp_ie_fieldtype

- **表名称：** 提取字段类型-主表
- **表名：** t_cvp_ie_fieldtype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 类型名称 | varchar | 50 |  | √ | ' ' | 类型名称 |
| 3 | fstatus | 数据状态 | varchar | 50 |  |  | null | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  |  | null | 人员 bos_user |
| 5 | fcreatorid | 创建人 | int8 | 64 |  |  | null | 人员 bos_user |
| 6 | fmasterid | 主数据内码 | int8 | 64 |  |  | null | 主数据内码 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fenable | 使用状态 | varchar | 50 |  |  | null | 使用状态,枚举: 0 :禁用 1 :可用 |
| 9 | ftypes | 类型 | varchar | 50 |  |  | null | 类型,枚举: 1 :通用文本 2 :纯数字 3 :邮箱 4 :小写金额 5 :大写金额 6 :公司名称 7 :姓名 8 :银行 9 :地址 10 :数字/英文 11 :日期 12 :币种 13 :电话号码 |
| 10 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cvp_ie_fieldtype |  | fid |
| 2 | idx_t_cvp_ie_fieldtype |  | fnumber,ftypes |
