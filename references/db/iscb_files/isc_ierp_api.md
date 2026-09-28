# 接口方案-isc_ierp_api

## 接口方案-多语言表 t_isc_guide_l

- **表名称：** 接口方案-多语言表
- **表名：** t_isc_guide_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 200 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 36 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 200 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 20 |  | √ | ' ' | pkid |
| 6 | fschedulename | fschedulename | varchar | 255 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_isc_guide_l_fid |  | fid,flocaleid |
| 2 | t_isc_guide_l_pkey |  | fpkid |

---

## 接口方案-主表 t_isc_guide

- **表名称：** 接口方案-主表
- **表名：** t_isc_guide

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | finterfacename_1 | finterfacename_1 | varchar | 100 |  | √ | ' ' |  |
| 3 | finterfacename_2 | finterfacename_2 | varchar | 100 |  | √ | ' ' |  |
| 4 | fgroupid | fgroupid | int8 | 64 |  | √ | 0 |  |
| 5 | finterfacename_3 | finterfacename_3 | varchar | 100 |  | √ | ' ' |  |
| 6 | finterfacename_4 | finterfacename_4 | varchar | 100 |  | √ | ' ' |  |
| 7 | finterfacename_5 | finterfacename_5 | varchar | 100 |  | √ | ' ' |  |
| 8 | finterfacename_6 | finterfacename_6 | varchar | 100 |  | √ | ' ' |  |
| 9 | finterfacename_7 | finterfacename_7 | varchar | 100 |  | √ | ' ' |  |
| 10 | fhandlerclass | 数据处理类 | varchar | 100 |  | √ | ' ' | 数据处理类 |
| 11 | finterfacename_8 | finterfacename_8 | varchar | 100 |  | √ | ' ' |  |
| 12 | finterfacename_9 | finterfacename_9 | varchar | 100 |  | √ | ' ' |  |
| 13 | feasentity | feasentity | int8 | 64 |  | √ | 0 |  |
| 14 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 15 | fstatus | fstatus | bpchar | 1 |  | √ | '0' |  |
| 16 | fcreatedate | fcreatedate | timestamp | 0 |  |  | null |  |
| 17 | fbizcloud | fbizcloud | varchar | 80 |  | √ | ' ' |  |
| 18 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 20 | fmodifydate | fmodifydate | timestamp | 0 |  |  | null |  |
| 21 | flocalsystem | 目标系统 | int8 | 64 |  | √ | 0 | [外部集成信息（废弃） isc_sysconn](../iscb_files/isc_sysconn.md) |
| 22 | fcreater | fcreater | int8 | 64 |  | √ | 0 |  |
| 23 | fmqlinkscheme | fmqlinkscheme | int8 | 64 |  | √ | 0 |  |
| 24 | fcustomeassolution | 通用接口服务名称 | varchar | 100 |  | √ | ' ' | 通用接口服务名称 |
| 25 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 26 | fbizapp | fbizapp | varchar | 80 |  | √ | ' ' |  |
| 27 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 28 | frepushdata | frepushdata | bpchar | 1 |  | √ | '0' |  |
| 29 | fmodifier | fmodifier | int8 | 64 |  | √ | 0 |  |
| 30 | fdescription | fdescription | varchar | 100 |  | √ | ' ' |  |
| 31 | feassolution | 通用接口服务名称 | varchar | 100 |  | √ | ' ' | 通用接口服务名称,枚举: |
| 32 | fremotesystem | fremotesystem | int8 | 64 |  | √ | 0 |  |
| 33 | fusemq | fusemq | int8 | 64 |  | √ | 1 |  |
| 34 | fbasedatafield | fbasedatafield | varchar | 80 |  | √ | ' ' |  |
| 35 | fenable | 使用状态 | int8 | 64 |  | √ | 1 | 使用状态,枚举: 0 :禁用 1 :可用 |
| 36 | fnumber | 编码 | varchar | 100 |  | √ | ' ' | 编码 |
| 37 | fvalueradio | fvalueradio | int8 | 64 |  | √ | 0 |  |
| 38 | ffiltercontext | ffiltercontext | text | 0 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_isc_guide_fnum |  | fnumber |
| 2 | t_isc_guide_pkey |  | fid |
