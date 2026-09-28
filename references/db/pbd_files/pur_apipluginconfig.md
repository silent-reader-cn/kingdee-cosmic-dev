# 接口插件配置-pur_apipluginconfig

## 接口插件配置-多语言表 t_pur_apipluginconfig_l

- **表名称：** 接口插件配置-多语言表
- **表名：** t_pur_apipluginconfig_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | fremark | varchar | 255 |  | √ | ' ' |  |
| 3 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_apiplugincfg_l_fid |  | fid,flocaleid |
| 2 | t_pur_apipluginconfig_l_pkey |  | fpkid |

---

## 接口插件配置-主表 t_pur_apipluginconfig

- **表名称：** 接口插件配置-主表
- **表名：** t_pur_apipluginconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | fcreateorgid | int8 | 64 |  | √ | 0 |  |
| 3 | fremark | fremark | varchar | 255 |  | √ | ' ' |  |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fname | fname | varchar | 100 |  | √ | ' ' |  |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 8 | fenablelog | fenablelog | bpchar | 1 |  | √ | ' ' |  |
| 9 | fentitykey | 表单标识 | varchar | 50 |  | √ | ' ' | 表单标识 |
| 10 | fdisabledate | fdisabledate | timestamp | 0 |  |  | null |  |
| 11 | fdisablerid | fdisablerid | int8 | 64 |  | √ | 0 |  |
| 12 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fctrlstrategy | fctrlstrategy | bpchar | 1 |  | √ | ' ' |  |
| 15 | fapiname | 接口名称 | varchar | 100 |  | √ | ' ' | 接口名称 |
| 16 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 17 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 18 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fenable | 可用状态 | bpchar | 1 |  | √ | ' ' | 可用状态,枚举: 0 :禁用 1 :可用 |
| 20 | fplugin | 插件 | varchar | 100 |  | √ | ' ' | 插件 |
| 21 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 22 | fuseorgid | fuseorgid | int8 | 64 |  | √ | 0 |  |
| 23 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_apipluginconfig_pkey |  | fid |
| 2 | idx_pur_apiplugin_fnumber |  | fnumber |
| 3 | idx_pur_apiplugin_fmasterid |  | fmasterid |
