# API网关标识-xkopenapi_gateway

## API网关标识-主表 t_open_apiservice

- **表名称：** API网关标识-主表
- **表名：** t_open_apiservice

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fallowguest | fallowguest | bpchar | 1 |  | √ | '0' |  |
| 3 | fdisabledate | fdisabledate | timestamp | 0 |  |  | null |  |
| 4 | fisfailcontinue | fisfailcontinue | bpchar | 1 |  | √ | '1' |  |
| 5 | fisvid | fisvid | varchar | 20 |  | √ | ' ' |  |
| 6 | foutputparam | foutputparam | varchar | 255 |  | √ | ' ' |  |
| 7 | fis_sys_api | fis_sys_api | bpchar | 1 |  | √ | '0' |  |
| 8 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 9 | fapideftype | fapideftype | varchar | 50 |  | √ | '0' |  |
| 10 | findigesttemplate | findigesttemplate | varchar | 255 |  | √ | ' ' |  |
| 11 | fcustomsort | fcustomsort | int8 | 64 |  | √ | 0 |  |
| 12 | fstdmodifytime | fstdmodifytime | timestamp | 0 |  |  | LOCALTIMESTAMP |  |
| 13 | fplugin | fplugin | text | 0 |  |  | null |  |
| 14 | foperation | foperation | varchar | 100 |  |  | null |  |
| 15 | isfailcontinue | isfailcontinue | bpchar | 1 |  | √ | '1' |  |
| 16 | fversion | fversion | varchar | 50 |  | √ | ' ' |  |
| 17 | fname | fname | varchar | 255 |  | √ | ' ' |  |
| 18 | fcosmicver | fcosmicver | varchar | 50 |  | √ | '5.0.002' |  |
| 19 | fcustommethod | fcustommethod | varchar | 100 |  |  | null |  |
| 20 | fcontenttype | fcontenttype | bpchar | 1 |  | √ | '0' |  |
| 21 | faddedinfo | faddedinfo | varchar | 255 |  | √ | ' ' |  |
| 22 | fdisablerid | fdisablerid | int8 | 64 |  |  | null |  |
| 23 | fhttpmethod | fhttpmethod | bpchar | 1 |  | √ | '0' |  |
| 24 | fis_only_thirdapp_auth | fis_only_thirdapp_auth | bpchar | 1 |  | √ | '0' |  |
| 25 | freqtype | freqtype | int8 | 64 |  |  | null |  |
| 26 | fgroup | fgroup | int8 | 64 |  | √ | 0 |  |
| 27 | fapiservicetype | fapiservicetype | bpchar | 1 |  | √ | '0' |  |
| 28 | fisdyobjresult | fisdyobjresult | bpchar | 1 |  | √ | '0' |  |
| 29 | fenable | fenable | bpchar | 1 |  | √ | '0' |  |
| 30 | forder_by_hide | forder_by_hide | varchar | 2000 |  | √ | ' ' |  |
| 31 | fnumber | fnumber | varchar | 150 |  | √ | ' ' |  |
| 32 | fprescript | fprescript | varchar | 255 |  |  | ' ' |  |
| 33 | fprescript_tag | fprescript_tag | text | 0 |  |  | null |  |
| 34 | fmethodname | fmethodname | varchar | 50 |  | √ | ' ' |  |
| 35 | finputparam | finputparam | varchar | 255 |  | √ | ' ' |  |
| 36 | fcu_limit_tac | fcu_limit_tac | int4 | 32 |  | √ | 0 |  |
| 37 | freptype | freptype | int8 | 64 |  |  | null |  |
| 38 | foutdigesttemplate | foutdigesttemplate | varchar | 255 |  | √ | ' ' |  |
| 39 | ffilterparam | ffilterparam | varchar | 2000 |  |  | ' ' |  |
| 40 | fappid | fappid | varchar | 36 |  |  | null |  |
| 41 | fplugintype | fplugintype | bpchar | 1 |  |  | '0' |  |
| 42 | furlformat | furlformat | varchar | 400 |  | √ | ' ' |  |
| 43 | fcheck_repeat_req | fcheck_repeat_req | bpchar | 1 |  | √ | '0' |  |
| 44 | fstatus | fstatus | bpchar | 1 |  | √ | 'A' |  |
| 45 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 46 | fmasterid | fmasterid | int8 | 64 |  | √ | 0 |  |
| 47 | fnamespace | fnamespace | varchar | 255 |  | √ | ' ' |  |
| 48 | fwsmethodname | fwsmethodname | varchar | 60 |  | √ | ' ' |  |
| 49 | fmessagetype | fmessagetype | varchar | 20 |  |  | null |  |
| 50 | fisdesensitize | fisdesensitize | bpchar | 1 |  | √ | '0' |  |
| 51 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 52 | fisoutparawithoutstatus | fisoutparawithoutstatus | bpchar | 1 |  | √ | '0' |  |
| 53 | forg_author_filter | forg_author_filter | bpchar | 1 |  | √ | '0' |  |
| 54 | fcreatetime | fcreatetime | timestamp | 0 |  | √ | LOCALTIMESTAMP |  |
| 55 | fbizobject | fbizobject | varchar | 36 |  | √ | ' ' |  |
| 56 | fclassname | fclassname | varchar | 255 |  | √ | ' ' |  |
| 57 | fsaveoperation | fsaveoperation | varchar | 2000 |  |  | null |  |
| 58 | fselectparam | fselectparam | varchar | 2000 |  |  | ' ' |  |
| 59 | faddedinfo_tag | faddedinfo_tag | text | 0 |  |  | null |  |
| 60 | fdiscription | fdiscription | varchar | 500 |  | √ | ' ' |  |
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

## API网关标识-分表 t_open_apiservice_x

- **表名称：** API网关标识-分表
- **表名：** t_open_apiservice_x

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fisgalaxy | fisgalaxy | bpchar | 1 |  | √ | '0' |  |
| 3 | fgatewayid | 网关侧API主键id | varchar | 50 |  | √ | ' ' | 网关侧API主键id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pk_t_open_apiservice_x |  | fisgalaxy |
| 2 | pk_t_open_apiservice_x |  | fid |
