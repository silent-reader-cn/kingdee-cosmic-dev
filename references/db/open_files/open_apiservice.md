# API服务（AI）-open_apiservice

## API服务（AI）-主表 t_open_apiservice

- **表名称：** API服务（AI）-主表
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
| 15 | foperation | 操作 | varchar | 100 |  |  | null | 操作,枚举: |
| 16 | fisasync | fisasync | bpchar | 1 |  | √ | '0' |  |
| 17 | isfailcontinue | isfailcontinue | bpchar | 1 |  | √ | '1' |  |
| 18 | fversion | fversion | varchar | 50 |  | √ | ' ' |  |
| 19 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 20 | fcosmicver | fcosmicver | varchar | 50 |  | √ | '5.0.002' |  |
| 21 | fcustommethod | 自定义方法 | varchar | 100 |  |  | null | 自定义方法 |
| 22 | fcontenttype | 内容格式 | bpchar | 1 |  | √ | '0' | 内容格式,枚举: 0 :application/json |
| 23 | faddedinfo | faddedinfo | varchar | 255 |  | √ | ' ' |  |
| 24 | fdisablerid | fdisablerid | int8 | 64 |  |  | null |  |
| 25 | fhttpmethod | 请求方式 | bpchar | 1 |  | √ | '0' | 请求方式,枚举: 0 :GET 1 :POST |
| 26 | fis_only_thirdapp_auth | 第三方应用授权 | bpchar | 1 |  | √ | '0' | 第三方应用授权 |
| 27 | freqtype | 请求消息类型 | int8 | 64 |  |  | null | [API消息类型 open_messagetype](../open_files/open_messagetype.md) |
| 28 | fgroup | fgroup | int8 | 64 |  | √ | 0 |  |
| 29 | fapiservicetype | API服务类型 | bpchar | 1 |  | √ | '0' | API服务类型,枚举: 0 :操作服务 1 :AI服务 2 :自定义服务 |
| 30 | fisdyobjresult | fisdyobjresult | bpchar | 1 |  | √ | '0' |  |
| 31 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 32 | forder_by_hide | forder_by_hide | varchar | 2000 |  | √ | ' ' |  |
| 33 | fnumber | 服务操作码 | varchar | 150 |  | √ | ' ' | 服务操作码 |
| 34 | fprescript | fprescript | varchar | 255 |  |  | ' ' |  |
| 35 | fprescript_tag | fprescript_tag | text | 0 |  |  | null |  |
| 36 | fsup_mtz | fsup_mtz | bpchar | 1 |  | √ | '0' |  |
| 37 | fmethodname | fmethodname | varchar | 50 |  | √ | ' ' |  |
| 38 | finputparam | finputparam | varchar | 255 |  | √ | ' ' |  |
| 39 | fcu_limit_tac | fcu_limit_tac | int4 | 32 |  | √ | 0 |  |
| 40 | freptype | 响应消息类型 | int8 | 64 |  |  | null | [API消息类型 open_messagetype](../open_files/open_messagetype.md) |
| 41 | foutdigesttemplate | foutdigesttemplate | varchar | 255 |  | √ | ' ' |  |
| 42 | ffilterparam | ffilterparam | varchar | 2000 |  |  | ' ' |  |
| 43 | fis_saveop_checkperm | fis_saveop_checkperm | bpchar | 1 |  | √ | '0' |  |
| 44 | fappid | 所属应用 | varchar | 36 |  |  | null | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |
| 45 | fplugintype | fplugintype | bpchar | 1 |  |  | '0' |  |
| 46 | furlformat | 请求路径 | varchar | 400 |  | √ | ' ' | 请求路径 |
| 47 | fcheck_repeat_req | 防止重复请求 | bpchar | 1 |  | √ | '0' | 防止重复请求 |
| 48 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 49 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 50 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 51 | fnamespace | fnamespace | varchar | 255 |  | √ | ' ' |  |
| 52 | fwsmethodname | fwsmethodname | varchar | 60 |  | √ | ' ' |  |
| 53 | fmessagetype | fmessagetype | varchar | 20 |  |  | null |  |
| 54 | fisdesensitize | fisdesensitize | bpchar | 1 |  | √ | '0' |  |
| 55 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 56 | fisoutparawithoutstatus | fisoutparawithoutstatus | bpchar | 1 |  | √ | '0' |  |
| 57 | forg_author_filter | forg_author_filter | bpchar | 1 |  | √ | '0' |  |
| 58 | fcreatetime | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 59 | fbizobject | 业务对象 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 60 | fclassname | fclassname | varchar | 255 |  | √ | ' ' |  |
| 61 | fsaveoperation | fsaveoperation | varchar | 2000 |  |  | null |  |
| 62 | fselectparam | fselectparam | varchar | 2000 |  |  | ' ' |  |
| 63 | faddedinfo_tag | faddedinfo_tag | text | 0 |  |  | null |  |
| 64 | fdiscription | 描述 | varchar | 500 |  | √ | ' ' | 描述 |
| 65 | fmustparam | fmustparam | varchar | 2000 |  |  | ' ' |  |
| 66 | furl | url | varchar | 100 |  |  | null | url |
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

## AI命令分录-子表 t_open_apiservice_aicmd

- **表名称：** AI命令分录-子表
- **表名：** t_open_apiservice_aicmd

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int8 | 64 |  |  | null | 分录行号 |
| 3 | fainumber | AI命令操作码 | varchar | 100 |  |  | null | AI命令操作码 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_open_apiservice_aicmd |  | fid,fentryid,fainumber |
| 2 | t_open_apiservice_aicmd_pkey |  | fentryid |

---

## API服务（AI）-多语言表 t_open_apiservice_l

- **表名称：** API服务（AI）-多语言表
- **表名：** t_open_apiservice_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fdiscription | 描述 | varchar | 500 |  | √ | ' ' | 描述 |
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

## AI命令分录-多语言表 t_open_apiservice_aicmd_l

- **表名称：** AI命令分录-多语言表
- **表名：** t_open_apiservice_aicmd_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fainame | AI名称 | varchar | 100 |  | √ | ' ' | AI名称 |
| 2 | faidescription | AI命令描述 | varchar | 500 |  | √ | ' ' | AI命令描述 |
| 3 | flocaleid | flocaleid | varchar | 36 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_open_apiservice_aicmd_l |  | fentryid,flocaleid |
| 2 | pk_t_open_apiservice_aicmd_l |  | fpkid |
