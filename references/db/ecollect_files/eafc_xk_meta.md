# 集成对象-星空(停用)-eafc_xk_meta

## 集成对象-星空(停用)-主表 tk_eafc_xk_meta

- **表名称：** 集成对象-星空(停用)-主表
- **表名：** tk_eafc_xk_meta

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fk_eafc_request_type | 请求方式 | varchar | 50 |  | √ | ' ' | 请求方式,枚举: 1 :get 2 :post |
| 6 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fk_eafc_need_auth | 需要授权 | bpchar | 1 |  | √ | '0' | 需要授权 |
| 10 | fk_eafc_system | 集成系统 | int8 | 64 |  |  | null | [集成系统-星空(停用) eafc_xk_system](../ecollect_files/eafc_xk_system.md) |
| 11 | fk_eafc_url | 对象标识（URL） | varchar | 500 |  | √ | ' ' | 对象标识（URL） |
| 12 | fk_eafc_desc | 对象描述 | varchar | 50 |  | √ | ' ' | 对象描述 |
| 13 | fk_eafc_name | 对象名称 | varchar | 50 |  | √ | ' ' | 对象名称 |
| 14 | fbillno | 对象编码 | varchar | 30 |  | √ | ' ' | 对象编码 |
| 15 | fauditorid | 审核人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fk_eafc_meta_type | 对象类型 | varchar | 50 |  | √ | ' ' | 对象类型,枚举: 1 :授权接口 2 :数据清单接口 3 :文件下载接口 4 :应归总数接口 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__eafc_xk_meta |  | fid |

---

## 单据体-子表 tk_eafc_xk_meta_param

- **表名称：** 单据体-子表
- **表名：** tk_eafc_xk_meta_param

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fk_eafc_param_desc | 字段描述 | varchar | 50 |  | √ | ' ' | 字段描述 |
| 3 | fk_eafc_param_need | 是否必填 | bpchar | 1 |  | √ | '0' | 是否必填 |
| 4 | fk_eafc_param_name | 字段名 | varchar | 50 |  | √ | ' ' | 字段名 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fk_eafc_param_type | 字段类型 | varchar | 50 |  | √ | ' ' | 字段类型,枚举: 1 :字符串 2 :整数 |
| 7 | fk_eafc_default_value | 默认值 | varchar | 50 |  | √ | ' ' | 默认值 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx__eafc_xk_meta_param_fk |  | fid |
| 2 | pk__eafc_xk_meta_param |  | fentryid |
