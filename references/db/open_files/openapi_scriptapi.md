# 脚本服务-openapi_scriptapi

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

## 脚本服务-主表 t_open_apiservice

- **表名称：** 脚本服务-主表
- **表名：** t_open_apiservice

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fallowguest | fallowguest | bpchar | 1 |  | √ | '0' |  |
| 3 | fpermitemid | 权限项 | varchar | 50 |  | √ | ' ' | 权限项,枚举: |
| 4 | fdisabledate | fdisabledate | timestamp | 0 |  |  | null |  |
| 5 | fisfailcontinue | fisfailcontinue | bpchar | 1 |  | √ | '1' |  |
| 6 | fisvid | 开发商标识 | varchar | 20 |  | √ | ' ' | 开发商标识 |
| 7 | foutputparam | 输出参数名 | varchar | 255 |  | √ | ' ' | 输出参数名 |
| 8 | fis_sys_api | fis_sys_api | bpchar | 1 |  | √ | '0' |  |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fapideftype | API定义类型 | varchar | 50 |  | √ | '0' | API定义类型,枚举: |
| 11 | findigesttemplate | 入参日志记录模板 | varchar | 255 |  | √ | ' ' | 入参日志记录模板 |
| 12 | fcustomsort | 自定义分类 | int8 | 64 |  | √ | 0 | [自定义分类维护 openapi_custom_sort](../open_files/openapi_custom_sort.md) |
| 13 | fstdmodifytime | API发布时间 | timestamp | 0 |  |  | LOCALTIMESTAMP | API发布时间 |
| 14 | fplugin | 插件 | text | 0 |  |  | null | 插件 |
| 15 | foperation | foperation | varchar | 100 |  |  | null |  |
| 16 | fisasync | 接口类型 | bpchar | 1 |  | √ | '0' | 接口类型,枚举: 0 :同步 1 :异步 |
| 17 | isfailcontinue | isfailcontinue | bpchar | 1 |  | √ | '1' |  |
| 18 | fversion | 版本 | varchar | 50 |  | √ | ' ' | 版本,枚举: 1 :1.0 2 :2.0 |
| 19 | fname | API名称 | varchar | 255 |  | √ | ' ' | API名称 |
| 20 | fcosmicver | 适用版本号 | varchar | 50 |  | √ | '5.0.002' | 适用版本号 |
| 21 | fcustommethod | fcustommethod | varchar | 100 |  |  | null |  |
| 22 | fcontenttype | fcontenttype | bpchar | 1 |  | √ | '0' |  |
| 23 | faddedinfo | faddedinfo | varchar | 255 |  | √ | ' ' |  |
| 24 | fdisablerid | fdisablerid | int8 | 64 |  |  | null |  |
| 25 | fhttpmethod | 请求方式 | bpchar | 1 |  | √ | '0' | 请求方式,枚举: 0 :GET 1 :POST |
| 26 | fis_only_thirdapp_auth | 第三方应用授权 | bpchar | 1 |  | √ | '0' | 第三方应用授权 |
| 27 | freqtype | freqtype | int8 | 64 |  |  | null |  |
| 28 | fgroup | 分组 | int8 | 64 |  | √ | 0 | [分组 open_customgroup](../open_files/open_customgroup.md) |
| 29 | fapiservicetype | API服务类型 | bpchar | 1 |  | √ | '0' | API服务类型,枚举: 0 :操作服务 1 :AI服务 2 :自定义服务 3 :脚本服务 |
| 30 | fisdyobjresult | fisdyobjresult | bpchar | 1 |  | √ | '0' |  |
| 31 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 32 | forder_by_hide | forder_by_hide | varchar | 2000 |  | √ | ' ' |  |
| 33 | fnumber | API编码 | varchar | 150 |  | √ | ' ' | API编码 |
| 34 | fprescript | 脚本 | varchar | 255 |  |  | ' ' | 脚本 |
| 35 | fprescript_tag | 脚本_详情 | text | 0 |  |  | null | 脚本_详情 |
| 36 | fsup_mtz | fsup_mtz | bpchar | 1 |  | √ | '0' |  |
| 37 | fmethodname | fmethodname | varchar | 50 |  | √ | ' ' |  |
| 38 | finputparam | 输入参数名 | varchar | 255 |  | √ | ' ' | 输入参数名 |
| 39 | fcu_limit_tac | fcu_limit_tac | int4 | 32 |  | √ | 0 |  |
| 40 | freptype | freptype | int8 | 64 |  |  | null |  |
| 41 | foutdigesttemplate | 出参日志记录模板 | varchar | 255 |  | √ | ' ' | 出参日志记录模板 |
| 42 | ffilterparam | ffilterparam | varchar | 2000 |  |  | ' ' |  |
| 43 | fis_saveop_checkperm | fis_saveop_checkperm | bpchar | 1 |  | √ | '0' |  |
| 44 | fappid | 所属应用 | varchar | 36 |  |  | null | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |
| 45 | fplugintype | fplugintype | bpchar | 1 |  |  | '0' |  |
| 46 | furlformat | 请求地址 | varchar | 400 |  | √ | ' ' | 请求地址 |
| 47 | fcheck_repeat_req | 防止重复请求 | bpchar | 1 |  | √ | '0' | 防止重复请求 |
| 48 | fstatus | API状态 | bpchar | 1 |  | √ | 'A' | API状态,枚举: D :禁用 C :发布 B :维护 A :内测 |
| 49 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 50 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 51 | fnamespace | 命名空间 | varchar | 255 |  | √ | ' ' | 命名空间 |
| 52 | fwsmethodname | WSDL方法名 | varchar | 60 |  | √ | ' ' | WSDL方法名 |
| 53 | fmessagetype | fmessagetype | varchar | 20 |  |  | null |  |
| 54 | fisdesensitize | fisdesensitize | bpchar | 1 |  | √ | '0' |  |
| 55 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 56 | fisoutparawithoutstatus | 出参仅返回Data域 | bpchar | 1 |  | √ | '0' | 出参仅返回Data域 |
| 57 | forg_author_filter | forg_author_filter | bpchar | 1 |  | √ | '0' |  |
| 58 | fcreatetime | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 59 | fbizobject | 业务对象 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 60 | fclassname | fclassname | varchar | 255 |  | √ | ' ' |  |
| 61 | fsaveoperation | fsaveoperation | varchar | 2000 |  |  | null |  |
| 62 | fselectparam | fselectparam | varchar | 2000 |  |  | ' ' |  |
| 63 | faddedinfo_tag | faddedinfo_tag | text | 0 |  |  | null |  |
| 64 | fdiscription | 详细描述 | varchar | 500 |  | √ | ' ' | 详细描述 |
| 65 | fmustparam | fmustparam | varchar | 2000 |  |  | ' ' |  |
| 66 | furl | furl | varchar | 100 |  |  | null |  |
| 67 | fisksql | fisksql | bpchar | 1 |  | √ | '0' |  |

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

## 返回参数-多语言表 t_open_apirespentry_l

- **表名称：** 返回参数-多语言表
- **表名：** t_open_apirespentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 2 | frespexample | 示例 | varchar | 1000 |  | √ | ' ' | 示例 |
| 3 | frespdes | 说明 | varchar | 1000 |  | √ | ' ' | 说明 |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_open_apirespentry_l |  | fpkid |
| 2 | idx_t_open_apirespentry_l |  | fentryid,flocaleid |

---

## 脚本服务-多语言表 t_open_apiservice_l

- **表名称：** 脚本服务-多语言表
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

## 脚本服务-分表 t_open_apiservice_x

- **表名称：** 脚本服务-分表
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

## 错误码-多语言表 t_openapi_errorcodeentry_l

- **表名称：** 错误码-多语言表
- **表名：** t_openapi_errorcodeentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 2 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 4 | ferrorcodedesc | 描述 | varchar | 500 |  | √ | ' ' | 描述 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_openapi_errorcodeentry_l |  | fentryid,flocaleid |
| 2 | pk_t_openapi_errorcodeentry_l |  | fpkid |

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
| 6 | ferrorcodedesc | 描述 | varchar | 500 |  | √ | ' ' | 描述 |

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
| 2 | fheaderdes | 说明 | varchar | 1000 |  | √ | ' ' | 说明 |
| 3 | fheadervalue | 参数示例 | varchar | 1000 |  | √ | ' ' | 参数示例 |
| 4 | fheadername | 参数名称 | varchar | 50 |  | √ | ' ' | 参数名称 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fheaderdefaultvalue | 默认值 | varchar | 250 |  | √ | ' ' | 默认值 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

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

## 引用资源-子表 t_openapi_resourceentity

- **表名称：** 引用资源-子表
- **表名：** t_openapi_resourceentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fres_category | 资源类别 | varchar | 50 |  | √ | ' ' | 资源类别,枚举: openapi_apilist :操作API openapi_customapi :自定义API（Java开发） openapi_scriptapi :自定义API（脚本开发） |
| 3 | fres_ref | 引用类别 | int8 | 64 |  | √ | 0 | API服务 openapi_apilist |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fres_alias | 别名 | varchar | 150 |  | √ | ' ' | 别名 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_openapi_resourceentity |  | fentryid |
| 2 | idx_t_open_resource_id |  | fid |

---

## 请求体单据体-子表 t_open_apibodyentry

- **表名称：** 请求体单据体-子表
- **表名：** t_open_apibodyentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fis_mul_value | 多值 | bpchar | 1 |  | √ | '0' | 多值 |
| 3 | fbody_level | 层级 | varchar | 4 |  | √ | ' ' | 层级 |
| 4 | fispathvariable | 路径变量 | bpchar | 1 |  | √ | '0' | 路径变量 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fparamtype | 参数类型 | varchar | 100 |  | √ | ' ' | 参数类型,枚举: String :String Long :Long Integer :Integer Boolean :Boolean Decimal :Decimal Date :Date DateTime :DateTime Array :Array Array :Array Array :Array Any :Any Struct :Struct |
| 7 | fobjpropname | 对象属性 | varchar | 250 |  | √ | ' ' | 对象属性 |
| 8 | fbody_data_model | 数据模型 | varchar | 50 |  | √ | ' ' | 数据模型 |
| 9 | fparamname | 参数名称 | varchar | 100 |  | √ | ' ' | 参数名称 |
| 10 | fbodyparamdes | 说明 | varchar | 1000 |  | √ | ' ' | 说明 |
| 11 | fexample | 示例 | varchar | 500 |  | √ | ' ' | 示例 |
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

## 请求头部-多语言表 t_open_apiheaderentry_l

- **表名称：** 请求头部-多语言表
- **表名：** t_open_apiheaderentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fheaderdes | 说明 | varchar | 1000 |  | √ | ' ' | 说明 |
| 2 | fheadervalue | 参数示例 | varchar | 1000 |  | √ | ' ' | 参数示例 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_open_apiheadentry_l |  | fentryid,flocaleid |
| 2 | pk_t_open_apiheaderentry_l |  | fpkid |

---

## 请求体单据体-多语言表 t_open_apibodyentry_l

- **表名称：** 请求体单据体-多语言表
- **表名：** t_open_apibodyentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbodyparamdes | 说明 | varchar | 1000 |  | √ | ' ' | 说明 |
| 2 | fexample | 示例 | varchar | 500 |  | √ | ' ' | 示例 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_open_apibodyentry_l |  | fpkid |
| 2 | idx_t_open_apibodyentry_l |  | fentryid,flocaleid |

---

## 返回参数-子表 t_open_apirespentry

- **表名称：** 返回参数-子表
- **表名：** t_open_apirespentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frespparamtype | 参数类型 | varchar | 100 |  | √ | ' ' | 参数类型,枚举: String :String Long :Long Integer :Integer Boolean :Boolean Decimal :Decimal Date :Date DateTime :DateTime Array :Array Array :Array Array :Array |
| 3 | fresp_data_model | 数据模型 | varchar | 50 |  | √ | ' ' | 数据模型 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fresp_level | 层级 | varchar | 4 |  | √ | ' ' | 层级 |
| 6 | frespexample | 示例 | varchar | 1000 |  | √ | ' ' | 示例 |
| 7 | frespparammust | 必填 | varchar | 50 |  | √ | ' ' | 必填,枚举: 1 :是 0 :否 |
| 8 | frespparamname | 参数名称 | varchar | 100 |  | √ | ' ' | 参数名称 |
| 9 | fis_resp_mul_value | 多值 | bpchar | 1 |  | √ | '0' | 多值 |
| 10 | fis_resp_custom | 自定义参数 | bpchar | 1 |  | √ | '0' | 自定义参数 |
| 11 | fprivacy_transdatatag | 数据标签 | int8 | 64 |  | √ | 0 | [数据标签 privacy_transdatatag](../privacy_files/privacy_transdatatag.md) |
| 12 | frespobjpropname | 对象属性 | varchar | 250 |  | √ | ' ' | 对象属性 |
| 13 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 | pid |
| 14 | frespdes | 说明 | varchar | 1000 |  | √ | ' ' | 说明 |
| 15 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

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
