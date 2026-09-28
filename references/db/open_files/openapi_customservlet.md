# 自定义Servlet服务-openapi_customservlet

## 配置参数-子表 t_openapi_ext

- **表名称：** 配置参数-子表
- **表名：** t_openapi_ext

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fext_value | value | varchar | 500 |  | √ | ' ' | value |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fext_key | key | varchar | 50 |  | √ | ' ' | key |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_openapi_ext |  | fentryid |
| 2 | idx_openapi_ext_fid |  | fid |

---

## 自定义Servlet服务-主表 t_open_apiservice

- **表名称：** 自定义Servlet服务-主表
- **表名：** t_open_apiservice

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fallowguest | 匿名访问 | bpchar | 1 |  | √ | '0' | 匿名访问 |
| 3 | fdisabledate | fdisabledate | timestamp | 0 |  |  | null |  |
| 4 | fisfailcontinue | fisfailcontinue | bpchar | 1 |  | √ | '1' |  |
| 5 | fisvid | 开发商标识 | varchar | 20 |  | √ | ' ' | 开发商标识 |
| 6 | foutputparam | 输出参数名 | varchar | 255 |  | √ | ' ' | 输出参数名 |
| 7 | fis_sys_api | 是否系统级API | bpchar | 1 |  | √ | '0' | 是否系统级API |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fapideftype | fapideftype | varchar | 50 |  | √ | '0' |  |
| 10 | findigesttemplate | 入参日志记录模板 | varchar | 255 |  | √ | ' ' | 入参日志记录模板 |
| 11 | fcustomsort | 自定义分类 | int8 | 64 |  | √ | 0 | 自定义分类维护 openapi_custom_sort |
| 12 | fstdmodifytime | API发布时间 | timestamp | 0 |  |  | LOCALTIMESTAMP | API发布时间 |
| 13 | fplugin | fplugin | text | 0 |  |  | null |  |
| 14 | foperation | foperation | varchar | 100 |  |  | null |  |
| 15 | isfailcontinue | isfailcontinue | bpchar | 1 |  | √ | '1' |  |
| 16 | fversion | 版本 | varchar | 50 |  | √ | ' ' | 版本,枚举: 1 :1.0 2 :2.0 |
| 17 | fname | API名称 | varchar | 255 |  | √ | ' ' | API名称 |
| 18 | fcosmicver | 适用版本号 | varchar | 50 |  | √ | '5.0.002' | 适用版本号 |
| 19 | fcustommethod | fcustommethod | varchar | 100 |  |  | null |  |
| 20 | fcontenttype | fcontenttype | bpchar | 1 |  | √ | '0' |  |
| 21 | faddedinfo | faddedinfo | varchar | 255 |  | √ | ' ' |  |
| 22 | fdisablerid | fdisablerid | int8 | 64 |  |  | null |  |
| 23 | fhttpmethod | 请求方式 | bpchar | 1 |  | √ | '0' | 请求方式,枚举: 0 :GET 1 :POST 9 :ALL |
| 24 | fis_only_thirdapp_auth | 第三方应用授权 | bpchar | 1 |  | √ | '0' | 第三方应用授权 |
| 25 | freqtype | freqtype | int8 | 64 |  |  | null |  |
| 26 | fgroup | 分组 | int8 | 64 |  | √ | 0 | 分组 open_customgroup |
| 27 | fapiservicetype | API服务类型 | bpchar | 1 |  | √ | '0' | API服务类型,枚举: 0 :操作服务 1 :AI服务 2 :自定义服务 4 :自定义Servlet |
| 28 | fisdyobjresult | fisdyobjresult | bpchar | 1 |  | √ | '0' |  |
| 29 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 30 | forder_by_hide | forder_by_hide | varchar | 2000 |  | √ | ' ' |  |
| 31 | fnumber | API编码 | varchar | 150 |  | √ | ' ' | API编码 |
| 32 | fprescript | fprescript | varchar | 255 |  |  | ' ' |  |
| 33 | fprescript_tag | fprescript_tag | text | 0 |  |  | null |  |
| 34 | fmethodname | fmethodname | varchar | 50 |  | √ | ' ' |  |
| 35 | finputparam | 输入参数名 | varchar | 255 |  | √ | ' ' | 输入参数名 |
| 36 | fcu_limit_tac | fcu_limit_tac | int4 | 32 |  | √ | 0 |  |
| 37 | freptype | freptype | int8 | 64 |  |  | null |  |
| 38 | foutdigesttemplate | 出参日志记录模板 | varchar | 255 |  | √ | ' ' | 出参日志记录模板 |
| 39 | ffilterparam | ffilterparam | varchar | 2000 |  |  | ' ' |  |
| 40 | fappid | 所属应用 | varchar | 36 |  |  | null | 业务应用实体 bos_devportal_bizapp |
| 41 | fplugintype | fplugintype | bpchar | 1 |  |  | '0' |  |
| 42 | furlformat | 请求地址 | varchar | 400 |  | √ | ' ' | 请求地址 |
| 43 | fcheck_repeat_req | 防止重复请求 | bpchar | 1 |  | √ | '0' | 防止重复请求 |
| 44 | fstatus | API状态 | bpchar | 1 |  | √ | 'A' | API状态,枚举: A :内测 B :维护 C :发布 D :禁用 |
| 45 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 46 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 47 | fnamespace | 命名空间 | varchar | 255 |  | √ | ' ' | 命名空间 |
| 48 | fwsmethodname | WSDL方法名 | varchar | 60 |  | √ | ' ' | WSDL方法名 |
| 49 | fmessagetype | fmessagetype | varchar | 20 |  |  | null |  |
| 50 | fisdesensitize | fisdesensitize | bpchar | 1 |  | √ | '0' |  |
| 51 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 52 | fisoutparawithoutstatus | fisoutparawithoutstatus | bpchar | 1 |  | √ | '0' |  |
| 53 | forg_author_filter | forg_author_filter | bpchar | 1 |  | √ | '0' |  |
| 54 | fcreatetime | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 55 | fbizobject | fbizobject | varchar | 36 |  | √ | ' ' |  |
| 56 | fclassname | 类名 | varchar | 255 |  | √ | ' ' | 类名 |
| 57 | fsaveoperation | fsaveoperation | varchar | 2000 |  |  | null |  |
| 58 | fselectparam | fselectparam | varchar | 2000 |  |  | ' ' |  |
| 59 | faddedinfo_tag | faddedinfo_tag | text | 0 |  |  | null |  |
| 60 | fdiscription | 详细描述 | varchar | 500 |  | √ | ' ' | 详细描述 |
| 61 | fmustparam | fmustparam | varchar | 2000 |  |  | ' ' |  |
| 62 | furl | furl | varchar | 100 |  |  | null |  |
| 63 | fisksql | fisksql | bpchar | 1 |  | √ | '0' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_apiservice_urlformat |  | furlformat |
| 2 | idx_open_apiservice_fnumber |  | fnumber |
| 3 | t_open_apiservice_pkey |  | fid |

---

## 错误码-子表 t_openapi_errorcodeentry

- **表名称：** 错误码-子表
- **表名：** t_openapi_errorcodeentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ferrorcode | 错误码 | varchar | 50 |  | √ | ' ' | 错误码 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 |  |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | ferrorcodedesc | 描述 | varchar | 255 |  | √ | ' ' | 描述 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_openapi_errorcodeentry |  | fentryid |
| 2 | idx_openapi_errorcodeentry_fid |  | fid |

---

## 请求头部-子表 t_open_apiheaderentry

- **表名称：** 请求头部-子表
- **表名：** t_open_apiheaderentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fheaderdes | 说明 | varchar | 255 |  | √ | ' ' | 说明 |
| 3 | fheadervalue | 参数示例 | varchar | 50 |  | √ | ' ' | 参数示例 |
| 4 | fheadername | 参数名称 | varchar | 50 |  | √ | ' ' | 参数名称 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_open_apiheaderentry_pkey |  | fentryid |
| 2 | idx_t_open_apiheader_id |  | fid |

---

## 请求体-子表 t_open_apibodyentry

- **表名称：** 请求体-子表
- **表名：** t_open_apibodyentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fis_mul_value | 多值 | bpchar | 1 |  | √ | '0' | 多值 |
| 3 | fbody_level | 层级 | varchar | 4 |  | √ | ' ' | 层级 |
| 4 | fispathvariable | fispathvariable | bpchar | 1 |  | √ | '0' |  |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fparamtype | 参数类型 | varchar | 100 |  | √ | ' ' | 参数类型,枚举: String :String Long :Long Integer :Integer Boolean :Boolean Decimal :Decimal Date :Date DateTime :DateTime Array :Array Array :Array Array :Array Entries :Entries Flex :Flex Any :Any Struct :Struct |
| 7 | fobjpropname | 对象属性 | varchar | 250 |  | √ | ' ' | 对象属性 |
| 8 | fbody_data_model | 数据模型 | varchar | 50 |  | √ | ' ' | 数据模型 |
| 9 | fparamname | 参数名称 | varchar | 100 |  | √ | ' ' | 参数名称 |
| 10 | fbodyparamdes | 说明 | varchar | 255 |  | √ | ' ' | 说明 |
| 11 | fexample | 示例 | varchar | 100 |  | √ | ' ' | 示例 |
| 12 | fdefaultvalue | 默认值 | varchar | 255 |  | √ | ' ' | 默认值 |
| 13 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 | pid |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 15 | fis_unique_key | 候选键 | bpchar | 1 |  | √ | '0' | 候选键 |
| 16 | fmust | 必填 | varchar | 50 |  | √ | ' ' | 必填,枚举: 1 :是 0 :否 |
| 17 | fis_body_custom | 自定义参数 | bpchar | 1 |  | √ | '0' | 自定义参数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_open_apibody_pentryid |  | fparententryid |
| 2 | idx_t_open_apibody_id |  | fid |
| 3 | t_open_apibodyentry_pkey |  | fentryid |

---

## 自定义Servlet服务-多语言表 t_open_apiservice_l

- **表名称：** 自定义Servlet服务-多语言表
- **表名：** t_open_apiservice_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | API名称 | varchar | 255 |  | √ | ' ' | API名称 |
| 3 | fdiscription | 详细描述 | varchar | 500 |  | √ | ' ' | 详细描述 |
| 4 | flocaleid | flocaleid | varchar | 36 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_open_apiservice_l |  | fpkid |
| 2 | idx_open_apiservice_l |  | fid,flocaleid |

---

## 自定义Servlet服务-分表 t_open_apiservice_x

- **表名称：** 自定义Servlet服务-分表
- **表名：** t_open_apiservice_x

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fisgalaxy | 是否星空 | bpchar | 1 |  | √ | '0' | 是否星空 |
| 3 | fgatewayid | fgatewayid | varchar | 50 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pk_t_open_apiservice_x |  | fisgalaxy |
| 2 | pk_t_open_apiservice_x |  | fid |

---

## 返回参数-子表 t_open_apirespentry

- **表名称：** 返回参数-子表
- **表名：** t_open_apirespentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frespparamtype | 参数类型 | varchar | 100 |  | √ | ' ' | 参数类型,枚举: String :String Long :Long Integer :Integer Boolean :Boolean Decimal :Decimal Date :Date DateTime :DateTime Array :Array Array :Array Array :Array Entries :Entries Flex :Flex |
| 3 | fresp_data_model | 数据模型 | varchar | 50 |  | √ | ' ' | 数据模型 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fresp_level | 层级 | varchar | 4 |  | √ | ' ' | 层级 |
| 6 | frespexample | 示例 | varchar | 100 |  | √ | ' ' | 示例 |
| 7 | frespparammust | 必填 | varchar | 50 |  | √ | ' ' | 必填,枚举: 1 :是 0 :否 |
| 8 | frespparamname | 参数名称 | varchar | 100 |  | √ | ' ' | 参数名称 |
| 9 | fis_resp_mul_value | 多值 | bpchar | 1 |  | √ | '0' | 多值 |
| 10 | fis_resp_custom | 自定义参数 | bpchar | 1 |  | √ | '0' | 自定义参数 |
| 11 | frespobjpropname | 对象属性 | varchar | 250 |  | √ | ' ' | 对象属性 |
| 12 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 | pid |
| 13 | frespdes | 说明 | varchar | 255 |  | √ | ' ' | 说明 |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_open_apirespentry_pkey |  | fentryid |
| 2 | idx_t_open_apiresp_pentryid |  | fparententryid |
| 3 | idx_t_open_apiresp_id |  | fid |
