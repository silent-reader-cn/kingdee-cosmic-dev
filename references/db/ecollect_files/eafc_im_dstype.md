# 数据源类型-eafc_im_dstype

## 请求单据体-子表 tk_eafc_im_dstype_in

- **表名称：** 请求单据体-子表
- **表名：** tk_eafc_im_dstype_in

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fk_eafc_param_desc | 字段描述 | varchar | 500 |  | √ | ' ' | 字段描述 |
| 3 | fk_eafc_param_need | 是否必填 | bpchar | 1 |  | √ | '0' | 是否必填 |
| 4 | fk_eafc_param_name | 字段名 | varchar | 50 |  | √ | ' ' | 字段名 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fk_eafc_param_type | 字段类型 | varchar | 50 |  | √ | ' ' | 字段类型,枚举: 1 :字符串 2 :整数 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx__eafc_im_dstype_in_fk |  | fid |
| 2 | pk__eafc_im_dstype_in |  | fentryid |

---

## 数据源类型-多语言表 tk_eafc_im_dstype_l

- **表名称：** 数据源类型-多语言表
- **表名：** tk_eafc_im_dstype_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 类型名称 | varchar | 50 |  | √ | ' ' | 类型名称 |
| 3 | flocaleid | flocaleid | varchar | 50 |  | √ | null | localeid |
| 4 | fpkid | fpkid | varchar | 50 |  | √ | null | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_eafc_im_dstype_l |  | fpkid |

---

## 数据源类型-主表 tk_eafc_im_dstype

- **表名称：** 数据源类型-主表
- **表名：** tk_eafc_im_dstype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fname | fname | varchar | 50 |  |  | null |  |
| 5 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fmasterid | 主数据内码 | int8 | 64 |  |  | null | 主数据内码 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 9 | fnumber | 类型编码 | varchar | 30 |  | √ | ' ' | 类型编码 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__eafc_im_dstype |  | fid |

---

## 响应单据体-子表 tk_eafc_im_dstype_out

- **表名称：** 响应单据体-子表
- **表名：** tk_eafc_im_dstype_out

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fk_eafc_param_desc | 字段描述 | varchar | 500 |  | √ | ' ' | 字段描述 |
| 3 | fk_eafc_param_need | 是否必填 | bpchar | 1 |  | √ | '0' | 是否必填 |
| 4 | fk_eafc_param_name | 字段名 | varchar | 50 |  | √ | ' ' | 字段名 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fk_eafc_param_type | 字段类型 | varchar | 50 |  | √ | ' ' | 字段类型,枚举: 1 :字符串 2 :整数 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | null | id |
| 8 | fk_eafc_res_businesstype | 所属内容 | int8 | 64 |  |  | null | [资料形式（三级类别） eafc_business_type](../ebase_files/eafc_business_type.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__eafc_im_dstype_out |  | fentryid |
| 2 | idx__eafc_im_dstype_out_fk |  | fid |
