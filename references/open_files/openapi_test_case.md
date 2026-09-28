# 测试用例-openapi_test_case

## 测试用例-多语言表 t_openapi_test_case_l

- **表名称：** 测试用例-多语言表
- **表名：** t_openapi_test_case_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 用例名称 | varchar | 50 |  | √ | ' ' | 用例名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_openapi_test_case_l |  | fpkid |
| 2 | idx_t_openapi_test_case_l_fid |  | fid |

---

## HTTP状态码-子表 t_openapi_test_hc_entry

- **表名称：** HTTP状态码-子表
- **表名：** t_openapi_test_hc_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fishttpcodecheck | 是否校验 | bpchar | 1 |  | √ | '0' | 是否校验 |
| 3 | fhttpcode | HTTP状态码 | varchar | 50 |  | √ | ' ' | HTTP状态码 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fhttpdes | 说明 | varchar | 255 |  | √ | ' ' | 说明 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_openapi_test_hc_entry |  | fentryid |
| 2 | idx_t_open_testhc_id |  | fid |

---

## Query参数单据体-子表 t_openapi_test_qp_entry

- **表名称：** Query参数单据体-子表
- **表名：** t_openapi_test_qp_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | furlparamkey | 参数名称 | varchar | 50 |  | √ | ' ' | 参数名称 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | furlparamvalue | 值 | varchar | 100 |  | √ | ' ' | 值 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | furlparamdes | 说明 | varchar | 255 |  | √ | ' ' | 说明 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_openapi_test_qp_entry |  | fentryid |
| 2 | idx_t_open_testquery_id |  | fid |

---

## 请求体单据体-子表 t_openapi_test_bd_entry

- **表名称：** 请求体单据体-子表
- **表名：** t_openapi_test_bd_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fparamvalue | 值 | varchar | 100 |  | √ | ' ' | 值 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 | pid |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fparamdes | 说明 | varchar | 255 |  | √ | ' ' | 说明 |
| 7 | fparamkey | 参数名称 | varchar | 100 |  | √ | ' ' | 参数名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_openapi_test_bd_entry |  | fentryid |
| 2 | idx_t_open_testbd_id |  | fid |

---

## 请求头单据体-子表 t_openapi_test_hd_entry

- **表名称：** 请求头单据体-子表
- **表名：** t_openapi_test_hd_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fheaderdes | 说明 | varchar | 255 |  | √ | ' ' | 说明 |
| 3 | fheadervalue | 参数值 | varchar | 50 |  | √ | ' ' | 参数值 |
| 4 | fheadername | 参数名称 | varchar | 50 |  | √ | ' ' | 参数名称 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_open_testheader_id |  | fid |
| 2 | pk_t_openapi_test_hd_entry |  | fentryid |

---

## 响应体-子表 t_openapi_test_rb_entry

- **表名称：** 响应体-子表
- **表名：** t_openapi_test_rb_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftypecheck | 类型校验 | bpchar | 1 |  | √ | '0' | 类型校验 |
| 3 | fmustcontain | 必含 | bpchar | 1 |  | √ | '0' | 必含 |
| 4 | fex_results | 预期结果 | varchar | 255 |  | √ | ' ' | 预期结果 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 | pid |
| 7 | frespkey | 参数名 | varchar | 50 |  | √ | ' ' | 参数名 |
| 8 | fcontentcheck | 内容包含校验 | bpchar | 1 |  | √ | '0' | 内容包含校验 |
| 9 | fcomparetype | 比较方式 | varchar | 50 |  | √ | ' ' | 比较方式,枚举: = :包含 != :不包含 in :在...中 not in :不在...中 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | fdatatype | 数据类型 | varchar | 50 |  | √ | ' ' | 数据类型,枚举: java.lang.String :String java.lang.Integer :Int java.lang.Long :Long java.lang.Boolean :Boolean Array :Array |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_openapi_test_rb_entry |  | fentryid |
| 2 | idx_t_open_testrb_id |  | fid |

---

## 测试用例-主表 t_openapi_test_case

- **表名称：** 测试用例-主表
- **表名：** t_openapi_test_case

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | 分类 | int8 | 64 |  | √ | 0 | 测试用例分组 openapi_test_case_group |
| 3 | fbd_type | 请求体类型 | varchar | 1 |  | √ | '2' | 请求体类型,枚举: 1 :form 2 :raw |
| 4 | fpriority | 优先级 | varchar | 1 |  | √ | ' ' | 优先级,枚举: 0 :P0 1 :P1 2 :P2 3 :P3 |
| 5 | fcreatestatus | 创建方式 | varchar | 1 |  | √ | '0' | 创建方式,枚举: 0 :手工创建 1 :API同步 |
| 6 | ftimelimit | 时间限制（ms） | int8 | 64 |  | √ | 0 | 时间限制（ms） |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 数据状态 | varchar | 1 |  | √ | '0' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fposscript | 后置脚本 | varchar | 255 |  |  | ' ' | 后置脚本 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fbd_text | 请求体json | varchar | 255 |  |  | ' ' | 请求体json |
| 13 | fapiid | API名称 | int8 | 64 |  | √ | 0 | API服务 openapi_apilist |
| 14 | ftimeoutcheck | 超时限制 | bpchar | 1 |  | √ | '0' | 超时限制 |
| 15 | ftimelimit_basis | 限时依据 | varchar | 1 |  | √ | ' ' | 限时依据,枚举: 1 :请求总时间 2 :首字节返回时间 |
| 16 | fposscript_tag | 后置脚本_详情 | text | 0 |  |  | null | 后置脚本_详情 |
| 17 | fremark | 用例说明 | varchar | 900 |  | √ | ' ' | 用例说明 |
| 18 | fname | 用例名称 | varchar | 50 |  | √ | ' ' | 用例名称 |
| 19 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 20 | fbd_text_tag | 请求体json_详情 | text | 0 |  |  | null | 请求体json_详情 |
| 21 | fcreatetime | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 22 | ftestrecord | 最近测试结果 | varchar | 1 |  | √ | ' ' | 最近测试结果,枚举: 0 :通过 1 :未通过 2 :暂无 |
| 23 | fenable | 使用状态 | varchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 24 | fnumber | 编码 | varchar | 150 |  | √ | ' ' | 编码 |
| 25 | fprescript | 前置脚本 | varchar | 255 |  |  | ' ' | 前置脚本 |
| 26 | fprescript_tag | 前置脚本_详情 | text | 0 |  |  | null | 前置脚本_详情 |
| 27 | ftesttime | 测试时间 | timestamp | 0 |  |  | null | 测试时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_openapi_testcase_num |  | fnumber |
| 2 | pk_t_openapi_test_case |  | fid |
