# API网关标识-xkopenapi_gateway

## API网关标识-主表 t_open_apiservice

- **表名称：** API网关标识-主表
- **表名：** t_open_apiservice

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fallowguest | fallowguest | bpchar | 1 |  | √ | '0' |  |
| 3 | fpermitemid | fpermitemid | varchar | 50 |  | √ | ' ' |  |
| 4 | fdisabledate | fdisabledate | timestamp | 0 |  |  | null |  |
| 5 | fisfailcontinue | fisfailcontinue | bpchar | 1 |  | √ | '1' |  |
| 6 | fisvid | fisvid | varchar | 20 |  | √ | ' ' |  |
| 7 | foutputparam | foutputparam | varchar | 255 |  | √ | ' ' |  |
| 8 | fis_sys_api | fis_sys_api | bpchar | 1 |  | √ | '0' |  |
| 9 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 10 | fapideftype | fapideftype | varchar | 50 |  | √ | '0' |  |
| 11 | findigesttemplate | findigesttemplate | varchar | 255 |  | √ | ' ' |  |
| 12 | fcustomsort | fcustomsort | int8 | 64 |  | √ | 0 |  |
| 13 | fstdmodifytime | fstdmodifytime | timestamp | 0 |  |  | LOCALTIMESTAMP |  |
| 14 | fplugin | fplugin | text | 0 |  |  | null |  |
| 15 | foperation | foperation | varchar | 100 |  |  | null |  |
| 16 | fisasync | fisasync | bpchar | 1 |  | √ | '0' |  |
| 17 | isfailcontinue | isfailcontinue | bpchar | 1 |  | √ | '1' |  |
| 18 | fversion | fversion | varchar | 50 |  | √ | ' ' |  |
| 19 | fname | fname | varchar | 255 |  | √ | ' ' |  |
| 20 | fcosmicver | fcosmicver | varchar | 50 |  | √ | '5.0.002' |  |
| 21 | fcustommethod | fcustommethod | varchar | 100 |  |  | null |  |
| 22 | fcontenttype | fcontenttype | bpchar | 1 |  | √ | '0' |  |
| 23 | faddedinfo | faddedinfo | varchar | 255 |  | √ | ' ' |  |
| 24 | fdisablerid | fdisablerid | int8 | 64 |  |  | null |  |
| 25 | fhttpmethod | fhttpmethod | bpchar | 1 |  | √ | '0' |  |
| 26 | fis_only_thirdapp_auth | fis_only_thirdapp_auth | bpchar | 1 |  | √ | '0' |  |
| 27 | freqtype | freqtype | int8 | 64 |  |  | null |  |
| 28 | fgroup | fgroup | int8 | 64 |  | √ | 0 |  |
| 29 | fapiservicetype | fapiservicetype | bpchar | 1 |  | √ | '0' |  |
| 30 | fisdyobjresult | fisdyobjresult | bpchar | 1 |  | √ | '0' |  |
| 31 | fenable | fenable | bpchar | 1 |  | √ | '0' |  |
| 32 | forder_by_hide | forder_by_hide | varchar | 2000 |  | √ | ' ' |  |
| 33 | fnumber | fnumber | varchar | 150 |  | √ | ' ' |  |
| 34 | fprescript | fprescript | varchar | 255 |  |  | ' ' |  |
| 35 | fprescript_tag | fprescript_tag | text | 0 |  |  | null |  |
| 36 | fsup_mtz | fsup_mtz | bpchar | 1 |  | √ | '0' |  |
| 37 | fmethodname | fmethodname | varchar | 50 |  | √ | ' ' |  |
| 38 | finputparam | finputparam | varchar | 255 |  | √ | ' ' |  |
| 39 | fcu_limit_tac | fcu_limit_tac | int4 | 32 |  | √ | 0 |  |
| 40 | freptype | freptype | int8 | 64 |  |  | null |  |
| 41 | foutdigesttemplate | foutdigesttemplate | varchar | 255 |  | √ | ' ' |  |
| 42 | ffilterparam | ffilterparam | varchar | 2000 |  |  | ' ' |  |
| 43 | fis_saveop_checkperm | fis_saveop_checkperm | bpchar | 1 |  | √ | '0' |  |
| 44 | fappid | fappid | varchar | 36 |  |  | null |  |
| 45 | fplugintype | fplugintype | bpchar | 1 |  |  | '0' |  |
| 46 | furlformat | furlformat | varchar | 400 |  | √ | ' ' |  |
| 47 | fcheck_repeat_req | fcheck_repeat_req | bpchar | 1 |  | √ | '0' |  |
| 48 | fstatus | fstatus | bpchar | 1 |  | √ | 'A' |  |
| 49 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 50 | fmasterid | fmasterid | int8 | 64 |  | √ | 0 |  |
| 51 | fnamespace | fnamespace | varchar | 255 |  | √ | ' ' |  |
| 52 | fwsmethodname | fwsmethodname | varchar | 60 |  | √ | ' ' |  |
| 53 | fmessagetype | fmessagetype | varchar | 20 |  |  | null |  |
| 54 | fisdesensitize | fisdesensitize | bpchar | 1 |  | √ | '0' |  |
| 55 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 56 | fisoutparawithoutstatus | fisoutparawithoutstatus | bpchar | 1 |  | √ | '0' |  |
| 57 | forg_author_filter | forg_author_filter | bpchar | 1 |  | √ | '0' |  |
| 58 | fcreatetime | fcreatetime | timestamp | 0 |  | √ | LOCALTIMESTAMP |  |
| 59 | fbizobject | fbizobject | varchar | 36 |  | √ | ' ' |  |
| 60 | fclassname | fclassname | varchar | 255 |  | √ | ' ' |  |
| 61 | fsaveoperation | fsaveoperation | varchar | 2000 |  |  | null |  |
| 62 | fselectparam | fselectparam | varchar | 2000 |  |  | ' ' |  |
| 63 | faddedinfo_tag | faddedinfo_tag | text | 0 |  |  | null |  |
| 64 | fdiscription | fdiscription | varchar | 500 |  | √ | ' ' |  |
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
