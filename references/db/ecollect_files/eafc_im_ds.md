# 集成数据源-eafc_im_ds

## 请求头单据体-子表 tk_eafc_im_ds_header

- **表名称：** 请求头单据体-子表
- **表名：** tk_eafc_im_ds_header

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fk_fpy_req_header_name | 参数名 | varchar | 255 |  | √ | ' ' | 参数名 |
| 3 | fk_fpy_req_header_desc | 参数描述 | varchar | 255 |  | √ | ' ' | 参数描述 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fk_fpy_req_header_value | 参数值 | varchar | 1024 |  | √ | ' ' | 参数值 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx__eafc_im_ds_header_fk |  | fid |
| 2 | pk__eafc_im_ds_header |  | fentryid |

---

## 集成数据源-多语言表 tk_eafc_im_ds_l

- **表名称：** 集成数据源-多语言表
- **表名：** tk_eafc_im_ds_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 数据源名称 | varchar | 50 |  | √ | ' ' | 数据源名称 |
| 3 | flocaleid | flocaleid | varchar | 50 |  | √ | null | localeid |
| 4 | fpkid | fpkid | varchar | 50 |  | √ | null | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_eafc_im_ds_l |  | fpkid |

---

## 集成数据源-主表 tk_eafc_im_ds

- **表名称：** 集成数据源-主表
- **表名：** tk_eafc_im_ds

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fk_eafc_ws_namespace | 命名空间 | varchar | 50 |  | √ | ' ' | 命名空间 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fgroupid | 集成系统 | int8 | 64 |  |  | null | [集成系统 eafc_im_system](../ecollect_files/eafc_im_system.md) |
| 5 | fname | fname | varchar | 50 |  |  | null |  |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fk_eafc_ws_method | 方法名 | varchar | 50 |  | √ | ' ' | 方法名 |
| 8 | fk_eafc_request_type | 请求方式 | varchar | 50 |  | √ | ' ' | 请求方式,枚举: 1 :GET 2 :POST |
| 9 | fk_eafc_interface_type | 接口类型 | varchar | 50 |  | √ | '1' | 接口类型,枚举: 1 :http 2 :WebService |
| 10 | fk_eafc_ds_desc | 数据源描述 | varchar | 500 |  | √ | ' ' | 数据源描述 |
| 11 | fk_eafc_request_url | 请求地址 | varchar | 500 |  | √ | ' ' | 请求地址 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fk_eafc_soap_action | SOAPAction | varchar | 50 |  | √ | ' ' | SOAPAction |
| 14 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fmasterid | 主数据内码 | int8 | 64 |  |  | null | 主数据内码 |
| 17 | fk_eafc_need_auth | 需要授权 | bpchar | 1 |  | √ | '1' | 需要授权 |
| 18 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 19 | fnumber | 数据源编码 | varchar | 30 |  | √ | ' ' | 数据源编码 |
| 20 | fk_eafc_im_dstype | 数据源类型 | int8 | 64 |  |  | null | [数据源类型 eafc_im_dstype](../ecollect_files/eafc_im_dstype.md) |
| 21 | fk_eafc_soap_type | SOAP协议 | varchar | 50 |  | √ | ' ' | SOAP协议,枚举: 1 :SOAP1.1 2 :SOAP1.2 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__eafc_im_ds |  | fid |

---

## 输入单据体-子表 tk_eafc_im_ds_in

- **表名称：** 输入单据体-子表
- **表名：** tk_eafc_im_ds_in

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fk_eafc_param_desc | 字段描述 | varchar | 500 |  | √ | ' ' | 字段描述 |
| 3 | fk_eafc_param_need | 是否必填 | bpchar | 1 |  | √ | '0' | 是否必填 |
| 4 | fk_eafc_param_name | 标准字段名 | varchar | 50 |  | √ | ' ' | 标准字段名 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fk_eafc_param_type | 字段类型 | varchar | 50 |  | √ | ' ' | 字段类型,枚举: string :字符串 int :整数 struct :结构 |
| 7 | fk_eafc_default_value | 默认值 | varchar | 500 |  | √ | ' ' | 默认值 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | null | id |
| 9 | fk_eafc_ds_param_name | 数据源字段名 | varchar | 50 |  | √ | ' ' | 数据源字段名 |
| 10 | fk_eafc_param_sysset | 是否系统预置 | bpchar | 1 |  | √ | '0' | 是否系统预置 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__eafc_im_ds_in |  | fentryid |
| 2 | idx__eafc_im_ds_in_fk |  | fid |

---

## 输出单据体-子表 tk_eafc_im_ds_out

- **表名称：** 输出单据体-子表
- **表名：** tk_eafc_im_ds_out

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fk_eafc_param_desc | 字段描述 | varchar | 500 |  | √ | ' ' | 字段描述 |
| 3 | fk_eafc_param_need | 是否必填 | bpchar | 1 |  | √ | '0' | 是否必填 |
| 4 | fk_eafc_param_name | 标准字段名 | varchar | 50 |  | √ | ' ' | 标准字段名 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fk_eafc_param_type | 字段类型 | varchar | 50 |  | √ | ' ' | 字段类型,枚举: 1 :字符串 2 :整数 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | null | id |
| 8 | fk_eafc_ds_param_name | 数据源字段名 | varchar | 50 |  | √ | ' ' | 数据源字段名 |
| 9 | fk_eafc_param_sysset | 是否系统预置 | bpchar | 1 |  | √ | '0' | 是否系统预置 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx__eafc_im_ds_out_fk |  | fid |
| 2 | pk__eafc_im_ds_out |  | fentryid |
