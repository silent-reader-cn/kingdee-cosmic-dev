# API服务（历史）-open_apiservice_new

## API服务（历史）-主表 t_open_apiservice

- **表名称：** API服务（历史）-主表
- **表名：** t_open_apiservice

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fallowguest | 匿名访问 | bpchar | 1 |  | √ | '0' | 匿名访问 |
| 3 | fpermitemid | fpermitemid | varchar | 50 |  | √ | ' ' |  |
| 4 | fdisabledate | fdisabledate | timestamp | 0 |  |  | null |  |
| 5 | fisfailcontinue | fisfailcontinue | bpchar | 1 |  | √ | '1' |  |
| 6 | fisvid | fisvid | varchar | 20 |  | √ | ' ' |  |
| 7 | foutputparam | foutputparam | varchar | 255 |  | √ | ' ' |  |
| 8 | fis_sys_api | 是否系统级API | bpchar | 1 |  | √ | '0' | 是否系统级API |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fapideftype | fapideftype | varchar | 50 |  | √ | '0' |  |
| 11 | findigesttemplate | findigesttemplate | varchar | 255 |  | √ | ' ' |  |
| 12 | fcustomsort | fcustomsort | int8 | 64 |  | √ | 0 |  |
| 13 | fstdmodifytime | fstdmodifytime | timestamp | 0 |  |  | LOCALTIMESTAMP |  |
| 14 | fplugin | 插件 | text | 0 |  |  | null | 插件 |
| 15 | foperation | 操作方式 | varchar | 100 |  |  | null | 操作方式,枚举: |
| 16 | fisasync | fisasync | bpchar | 1 |  | √ | '0' |  |
| 17 | isfailcontinue | isfailcontinue | bpchar | 1 |  | √ | '1' |  |
| 18 | fversion | 版本 | varchar | 50 |  | √ | ' ' | 版本,枚举: 1 :1.0 2 :2.0 |
| 19 | fname | API名称 | varchar | 255 |  | √ | ' ' | API名称 |
| 20 | fcosmicver | fcosmicver | varchar | 50 |  | √ | '5.0.002' |  |
| 21 | fcustommethod | 自定义方法 | varchar | 100 |  |  | null | 自定义方法 |
| 22 | fcontenttype | 内容格式 | bpchar | 1 |  | √ | '0' | 内容格式,枚举: 0 :application/json 1 :text/json |
| 23 | faddedinfo | faddedinfo | varchar | 255 |  | √ | ' ' |  |
| 24 | fdisablerid | fdisablerid | int8 | 64 |  |  | null |  |
| 25 | fhttpmethod | 请求方式 | bpchar | 1 |  | √ | '0' | 请求方式,枚举: 0 :GET 1 :POST |
| 26 | fis_only_thirdapp_auth | 第三方应用授权 | bpchar | 1 |  | √ | '0' | 第三方应用授权 |
| 27 | freqtype | freqtype | int8 | 64 |  |  | null |  |
| 28 | fgroup | fgroup | int8 | 64 |  | √ | 0 |  |
| 29 | fapiservicetype | API服务类型 | bpchar | 1 |  | √ | '0' | API服务类型,枚举: 0 :操作服务 1 :AI服务 2 :自定义服务 |
| 30 | fisdyobjresult | fisdyobjresult | bpchar | 1 |  | √ | '0' |  |
| 31 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 32 | forder_by_hide | forder_by_hide | varchar | 2000 |  | √ | ' ' |  |
| 33 | fnumber | API编号 | varchar | 150 |  | √ | ' ' | API编号 |
| 34 | fprescript | fprescript | varchar | 255 |  |  | ' ' |  |
| 35 | fprescript_tag | fprescript_tag | text | 0 |  |  | null |  |
| 36 | fsup_mtz | fsup_mtz | bpchar | 1 |  | √ | '0' |  |
| 37 | fmethodname | fmethodname | varchar | 50 |  | √ | ' ' |  |
| 38 | finputparam | finputparam | varchar | 255 |  | √ | ' ' |  |
| 39 | fcu_limit_tac | fcu_limit_tac | int4 | 32 |  | √ | 0 |  |
| 40 | freptype | freptype | int8 | 64 |  |  | null |  |
| 41 | foutdigesttemplate | foutdigesttemplate | varchar | 255 |  | √ | ' ' |  |
| 42 | ffilterparam | 过滤条件隐藏字段 | varchar | 2000 |  |  | ' ' | 过滤条件隐藏字段 |
| 43 | fis_saveop_checkperm | fis_saveop_checkperm | bpchar | 1 |  | √ | '0' |  |
| 44 | fappid | 所属应用 | varchar | 36 |  |  | null | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |
| 45 | fplugintype | fplugintype | bpchar | 1 |  |  | '0' |  |
| 46 | furlformat | 请求地址 | varchar | 400 |  | √ | ' ' | 请求地址 |
| 47 | fcheck_repeat_req | 防止重复请求 | bpchar | 1 |  | √ | '0' | 防止重复请求 |
| 48 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 49 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 50 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 51 | fnamespace | fnamespace | varchar | 255 |  | √ | ' ' |  |
| 52 | fwsmethodname | fwsmethodname | varchar | 60 |  | √ | ' ' |  |
| 53 | fmessagetype | fmessagetype | varchar | 20 |  |  | null |  |
| 54 | fisdesensitize | 是否脱敏 | bpchar | 1 |  | √ | '0' | 是否脱敏 |
| 55 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 56 | fisoutparawithoutstatus | fisoutparawithoutstatus | bpchar | 1 |  | √ | '0' |  |
| 57 | forg_author_filter | 插件用户权限校验 | bpchar | 1 |  | √ | '0' | 插件用户权限校验 |
| 58 | fcreatetime | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 59 | fbizobject | 业务对象 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 60 | fclassname | fclassname | varchar | 255 |  | √ | ' ' |  |
| 61 | fsaveoperation | fsaveoperation | varchar | 2000 |  |  | null |  |
| 62 | fselectparam | 查询隐藏字段 | varchar | 2000 |  |  | ' ' | 查询隐藏字段 |
| 63 | faddedinfo_tag | faddedinfo_tag | text | 0 |  |  | null |  |
| 64 | fdiscription | 详细描述 | varchar | 500 |  | √ | ' ' | 详细描述 |
| 65 | fmustparam | 必填字段（隐藏） | varchar | 2000 |  |  | ' ' | 必填字段（隐藏） |
| 66 | furl | furl | varchar | 100 |  |  | null |  |
| 67 | fisksql | 普通模式 | bpchar | 1 |  | √ | '0' | 普通模式 |

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

## 条件字段-子表 t_open_apiqueryfilter

- **表名称：** 条件字段-子表
- **表名：** t_open_apiqueryfilter

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffilterlink | 逻辑连接符 | varchar | 5 |  | √ | ' ' | 逻辑连接符,枚举: AND :与 OR :或 |
| 3 | ffilterleftbracket | 左括号 | varchar | 5 |  | √ | ' ' | 左括号,枚举: ( :( (( :(( |
| 4 | ffilter_constant | ffilter_constant | varchar | 255 |  | √ | ' ' |  |
| 5 | ffilterrightbracket | 右括号 | varchar | 5 |  | √ | ' ' | 右括号,枚举: ) :) )) :)) |
| 6 | ffiltercolumn | 条件字段 | varchar | 250 |  | √ | ' ' | 条件字段 |
| 7 | ffilter_type | ffilter_type | varchar | 50 |  | √ | ' ' |  |
| 8 | ffiltercompare | 比较方式 | varchar | 25 |  | √ | ' ' | 比较方式,枚举: = :等于 STARTS_WITH :开头是 CONTAINS :包含 ENDS_WITH :结尾是 > :大于 >= :大于或等于 < :小于 <= :小于或等于 <> :不等于 in :IN not in :NOT IN NOT_STARTS_WITH :开头不是 NOT_CONTAINS :不包含 NOT_ENDS_WITH :结尾不是 IS_NULL :为空 IS_NOT_NULL :不为空 |
| 9 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 10 | ffiltervalue | 比较变量 | varchar | 50 |  | √ | ' ' | 比较变量,枚举: |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 12 | ffilterlabel | 字段描述 | varchar | 1000 |  | √ | ' ' | 字段描述 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_open_apiqueryfilter |  | fentryid |
| 2 | idx_t_open_apiqueryfilter_id |  | fid |

---

## API服务（历史）-多语言表 t_open_apiservice_l

- **表名称：** API服务（历史）-多语言表
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

## 请求头单据体-子表 t_open_apiheaderentry

- **表名称：** 请求头单据体-子表
- **表名：** t_open_apiheaderentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fheaderdes | 说明 | varchar | 1000 |  | √ | ' ' | 说明 |
| 3 | fheadervalue | 参数值 | varchar | 1000 |  | √ | ' ' | 参数值 |
| 4 | fheadername | 参数名称 | varchar | 50 |  | √ | ' ' | 参数名称 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fheaderdefaultvalue | fheaderdefaultvalue | varchar | 250 |  | √ | ' ' |  |
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

## Query参数单据体-子表 t_open_apiqueryparamentry

- **表名称：** Query参数单据体-子表
- **表名：** t_open_apiqueryparamentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | furlparamtype | 参数类型 | varchar | 50 |  | √ | ' ' | 参数类型,枚举: String :String Float :Float Boolean :Boolean Long :Long int :int Double :Double Date :Date |
| 3 | furlparamname | 参数名称 | varchar | 50 |  | √ | ' ' | 参数名称 |
| 4 | furlparammust | 必填 | varchar | 50 |  | √ | ' ' | 必填,枚举: 1 :是 0 :否 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | furlparamdes | 说明 | varchar | 255 |  | √ | ' ' | 说明 |
| 8 | furlparamexample | 示例 | varchar | 50 |  | √ | ' ' | 示例 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_open_apiquery_id |  | fid |
| 2 | t_open_apiqueryparamentry_pkey |  | fentryid |

---

## 请求体单据体-子表 t_open_apibodyentry

- **表名称：** 请求体单据体-子表
- **表名：** t_open_apibodyentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fis_mul_value | fis_mul_value | bpchar | 1 |  | √ | '0' |  |
| 3 | fbody_level | fbody_level | varchar | 4 |  | √ | ' ' |  |
| 4 | fispathvariable | fispathvariable | bpchar | 1 |  | √ | '0' |  |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fparamtype | 参数类型 | varchar | 100 |  | √ | ' ' | 参数类型,枚举: String :String Long :Long int :int Boolean :Boolean Double :Double Float :Float Object :Object Array :Array |
| 7 | fobjpropname | fobjpropname | varchar | 250 |  | √ | ' ' |  |
| 8 | fbody_data_model | fbody_data_model | varchar | 50 |  | √ | ' ' |  |
| 9 | fparamname | 参数名称 | varchar | 100 |  | √ | ' ' | 参数名称 |
| 10 | fbodyparamdes | 说明 | varchar | 1000 |  | √ | ' ' | 说明 |
| 11 | fexample | 示例 | varchar | 500 |  | √ | ' ' | 示例 |
| 12 | fdefaultvalue | fdefaultvalue | varchar | 255 |  | √ | ' ' |  |
| 13 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 | pid |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 15 | fis_unique_key | fis_unique_key | bpchar | 1 |  | √ | '0' |  |
| 16 | fmust | 必填 | varchar | 50 |  | √ | ' ' | 必填,枚举: 1 :是 0 :否 |
| 17 | fis_body_custom | fis_body_custom | bpchar | 1 |  | √ | '0' |  |

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

## 返回参数-子表 t_open_apirespentry

- **表名称：** 返回参数-子表
- **表名：** t_open_apirespentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frespparamtype | 参数类型 | varchar | 100 |  | √ | ' ' | 参数类型,枚举: String :String Long :Long int :int Boolean :Boolean Double :Double Float :Float Object :Object Array :Array |
| 3 | fresp_data_model | fresp_data_model | varchar | 50 |  | √ | ' ' |  |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fresp_level | fresp_level | varchar | 4 |  | √ | ' ' |  |
| 6 | frespexample | 示例 | varchar | 1000 |  | √ | ' ' | 示例 |
| 7 | frespparammust | 必填 | varchar | 50 |  | √ | ' ' | 必填,枚举: 1 :是 0 :否 |
| 8 | frespparamname | 参数名称 | varchar | 100 |  | √ | ' ' | 参数名称 |
| 9 | fis_resp_mul_value | fis_resp_mul_value | bpchar | 1 |  | √ | '0' |  |
| 10 | fis_resp_custom | fis_resp_custom | bpchar | 1 |  | √ | '0' |  |
| 11 | fprivacy_transdatatag | fprivacy_transdatatag | int8 | 64 |  | √ | 0 |  |
| 12 | frespobjpropname | frespobjpropname | varchar | 250 |  | √ | ' ' |  |
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
