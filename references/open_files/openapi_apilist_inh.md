# API服务维护_继承-openapi_apilist_inh

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

## API服务维护_继承-主表 t_open_apiservice

- **表名称：** API服务维护_继承-主表
- **表名：** t_open_apiservice

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fallowguest | 匿名访问 | bpchar | 1 |  | √ | '0' | 匿名访问 |
| 3 | fdisabledate | fdisabledate | timestamp | 0 |  |  | null |  |
| 4 | fisfailcontinue | 失败后是否继续 | bpchar | 1 |  | √ | '1' | 失败后是否继续 |
| 5 | fisvid | 开发商标识 | varchar | 20 |  | √ | ' ' | 开发商标识 |
| 6 | foutputparam | 输出参数名 | varchar | 255 |  | √ | ' ' | 输出参数名 |
| 7 | fis_sys_api | 是否系统级API | bpchar | 1 |  | √ | '0' | 是否系统级API |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fapideftype | API定义类型 | varchar | 50 |  | √ | '0' | API定义类型,枚举: |
| 10 | findigesttemplate | 入参日志记录模板 | varchar | 255 |  | √ | ' ' | 入参日志记录模板 |
| 11 | fcustomsort | 自定义分类 | int8 | 64 |  | √ | 0 | 自定义分类维护 openapi_custom_sort |
| 12 | fstdmodifytime | API发布时间 | timestamp | 0 |  |  | LOCALTIMESTAMP | API发布时间 |
| 13 | fplugin | 插件 | text | 0 |  |  | null | 插件 |
| 14 | foperation | 操作方式 | varchar | 100 |  |  | null | 操作方式,枚举: |
| 15 | isfailcontinue | isfailcontinue | bpchar | 1 |  | √ | '1' |  |
| 16 | fversion | 版本 | varchar | 50 |  | √ | ' ' | 版本,枚举: 1 :1.0 2 :2.0 |
| 17 | fname | API名称 | varchar | 255 |  | √ | ' ' | API名称 |
| 18 | fcosmicver | 适用版本号 | varchar | 50 |  | √ | '5.0.002' | 适用版本号 |
| 19 | fcustommethod | 自定义方法 | varchar | 100 |  |  | null | 自定义方法 |
| 20 | fcontenttype | fcontenttype | bpchar | 1 |  | √ | '0' |  |
| 21 | faddedinfo | API附加说明字段 | varchar | 255 |  | √ | ' ' | API附加说明字段 |
| 22 | fdisablerid | fdisablerid | int8 | 64 |  |  | null |  |
| 23 | fhttpmethod | 请求方式 | bpchar | 1 |  | √ | '0' | 请求方式,枚举: 0 :GET 1 :POST 9 :ALL |
| 24 | fis_only_thirdapp_auth | 第三方应用授权 | bpchar | 1 |  | √ | '0' | 第三方应用授权 |
| 25 | freqtype | freqtype | int8 | 64 |  |  | null |  |
| 26 | fgroup | 分组 | int8 | 64 |  | √ | 0 | 分组 open_customgroup |
| 27 | fapiservicetype | API服务类型 | bpchar | 1 |  | √ | '0' | API服务类型,枚举: 0 :零代码配置 2 :Java插件 3 :脚本开发 4 :Servlet开发 |
| 28 | fisdyobjresult | 返回动态对象 | bpchar | 1 |  | √ | '0' | 返回动态对象 |
| 29 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 30 | forder_by_hide | 排序(隐藏) | varchar | 2000 |  | √ | ' ' | 排序(隐藏) |
| 31 | fnumber | API编码 | varchar | 150 |  | √ | ' ' | API编码 |
| 32 | fprescript | fprescript | varchar | 255 |  |  | ' ' |  |
| 33 | fprescript_tag | fprescript_tag | text | 0 |  |  | null |  |
| 34 | fmethodname | 方法名 | varchar | 50 |  | √ | ' ' | 方法名,枚举: |
| 35 | finputparam | 输入参数名 | varchar | 255 |  | √ | ' ' | 输入参数名 |
| 36 | fcu_limit_tac | fcu_limit_tac | int4 | 32 |  | √ | 0 |  |
| 37 | freptype | freptype | int8 | 64 |  |  | null |  |
| 38 | foutdigesttemplate | 出参日志记录模板 | varchar | 255 |  | √ | ' ' | 出参日志记录模板 |
| 39 | ffilterparam | 过滤条件隐藏字段 | varchar | 2000 |  |  | ' ' | 过滤条件隐藏字段 |
| 40 | fappid | 所属应用 | varchar | 36 |  |  | null | 业务应用实体 bos_devportal_bizapp |
| 41 | fplugintype | fplugintype | bpchar | 1 |  |  | '0' |  |
| 42 | furlformat | 请求地址 | varchar | 400 |  | √ | ' ' | 请求地址 |
| 43 | fcheck_repeat_req | 防止重复请求 | bpchar | 1 |  | √ | '0' | 防止重复请求 |
| 44 | fstatus | API状态 | bpchar | 1 |  | √ | 'A' | API状态,枚举: D :禁用 C :发布 B :维护 A :内测 |
| 45 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 46 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 47 | fnamespace | 命名空间 | varchar | 255 |  | √ | ' ' | 命名空间 |
| 48 | fwsmethodname | WSDL方法名 | varchar | 60 |  | √ | ' ' | WSDL方法名 |
| 49 | fmessagetype | fmessagetype | varchar | 20 |  |  | null |  |
| 50 | fisdesensitize | 是否脱敏 | bpchar | 1 |  | √ | '0' | 是否脱敏 |
| 51 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 52 | fisoutparawithoutstatus | 出参仅返回Data域 | bpchar | 1 |  | √ | '0' | 出参仅返回Data域 |
| 53 | forg_author_filter | 启用查询权限控制 | bpchar | 1 |  | √ | '0' | 启用查询权限控制 |
| 54 | fcreatetime | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 55 | fbizobject | 业务对象 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 56 | fclassname | 类名 | varchar | 255 |  | √ | ' ' | 类名 |
| 57 | fsaveoperation | 保存参数 | varchar | 2000 |  |  | null | 保存参数 |
| 58 | fselectparam | 查询隐藏字段 | varchar | 2000 |  |  | ' ' | 查询隐藏字段 |
| 59 | faddedinfo_tag | API附加说明字段_详情 | text | 0 |  |  | null | API附加说明字段_详情 |
| 60 | fdiscription | 详细描述 | varchar | 500 |  | √ | ' ' | 详细描述 |
| 61 | fmustparam | 必填字段（隐藏） | varchar | 2000 |  |  | ' ' | 必填字段（隐藏） |
| 62 | furl | furl | varchar | 100 |  |  | null |  |
| 63 | fisksql | 预览 | bpchar | 1 |  | √ | '0' | 预览 |

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

## 查询条件-子表 t_open_apiqueryfilter

- **表名称：** 查询条件-子表
- **表名：** t_open_apiqueryfilter

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffilterlink | 逻辑连接符 | varchar | 5 |  | √ | ' ' | 逻辑连接符,枚举: 0 :与 1 :或 |
| 3 | ffilterleftbracket | 左括号 | varchar | 5 |  | √ | ' ' | 左括号,枚举: ( :( (( :(( ((( :((( |
| 4 | ffilter_constant | 比较常量 | varchar | 255 |  | √ | ' ' | 比较常量 |
| 5 | ffilterrightbracket | 右括号 | varchar | 5 |  | √ | ' ' | 右括号,枚举: ) :) )) :)) ))) :))) |
| 6 | ffiltercolumn | 条件字段 | varchar | 250 |  | √ | ' ' | 条件字段 |
| 7 | ffilter_type | 字段类型 | varchar | 50 |  | √ | ' ' | 字段类型 |
| 8 | ffiltercompare | 比较方式 | varchar | 25 |  | √ | ' ' | 比较方式,枚举: |
| 9 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 10 | ffiltervalue | 比较变量 | varchar | 50 |  | √ | ' ' | 比较变量,枚举: |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 12 | ffilterlabel | 字段描述 | varchar | 255 |  | √ | ' ' | 字段描述 |

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

## 引用资源-子表 t_openapi_resourceentity

- **表名称：** 引用资源-子表
- **表名：** t_openapi_resourceentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fres_category | 资源类别 | varchar | 50 |  | √ | ' ' | 资源类别,枚举: openapi_apilist :API服务维护 |
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

## 排序分录-子表 t_open_apiorderby

- **表名称：** 排序分录-子表
- **表名：** t_open_apiorderby

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | forder_desc | 字段描述 | varchar | 255 |  | √ | ' ' | 字段描述 |
| 3 | forder_mode | 排序方式 | varchar | 50 |  | √ | ' ' | 排序方式,枚举: asc :顺序 desc :倒序 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | forder_field | 排序字段 | varchar | 250 |  | √ | ' ' | 排序字段 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_open_apiorderby |  | fentryid |
| 2 | idx_open_apiorderby_fk |  | fid |

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
| 4 | furlparammust | 必填 | varchar | 50 |  | √ | ' ' | 必填,枚举: 1 :是 |
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

## 请求体-子表 t_open_apibodyentry

- **表名称：** 请求体-子表
- **表名：** t_open_apibodyentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fis_mul_value | 多值 | bpchar | 1 |  | √ | '0' | 多值 |
| 3 | fbody_level | 层级 | varchar | 4 |  | √ | ' ' | 层级 |
| 4 | fispathvariable | 路径变量 | bpchar | 1 |  | √ | '0' | 路径变量 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fparamtype | 参数类型 | varchar | 100 |  | √ | ' ' | 参数类型,枚举: String :String Long :Long Integer :Integer Boolean :Boolean Decimal :Decimal Date :Date DateTime :DateTime Array :Array Array :Array Array :Array Entries :Entries Flex :Flex |
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

## API服务维护_继承-多语言表 t_open_apiservice_l

- **表名称：** API服务维护_继承-多语言表
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

## API服务维护_继承-分表 t_open_apiservice_x

- **表名称：** API服务维护_继承-分表
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
