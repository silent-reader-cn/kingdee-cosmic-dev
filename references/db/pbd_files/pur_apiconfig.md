# 系统集成配置-pur_apiconfig

## 系统集成配置-使用范围位图表 t_pur_apiconfig_m

- **表名称：** 系统集成配置-使用范围位图表
- **表名：** t_pur_apiconfig_m

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | forgid | forgid | int8 | 64 |  | √ | null |  |
| 2 | fdata | fdata | bytea | 0 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | forgid | forgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_pur_apiconfig_m |  | forgid |

---

## 系统集成配置-多语言表 t_pur_apiconfig_l

- **表名称：** 系统集成配置-多语言表
- **表名：** t_pur_apiconfig_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 3 | fname | 方案名称 | varchar | 100 |  | √ | ' ' | 方案名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_apiconfig_l_pkey |  | fpkid |
| 2 | idx_pur_apiconfig_l_fid |  | fid,flocaleid |

---

## 系统集成配置-使用范围表 t_pur_apiconfig_u

- **表名称：** 系统集成配置-使用范围表
- **表名：** t_pur_apiconfig_u

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcreateorgid | fcreateorgid | int8 | 64 |  |  | null |  |
| 2 | fdataid | fdataid | int8 | 64 |  | √ | null |  |
| 3 | fuseorgid | fuseorgid | int8 | 64 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdataid | fdataid,fuseorgid |
| 2 | fuseorgid | fdataid,fuseorgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_pur_apiconfig_u_uo |  | fuseorgid |
| 2 | t_pur_apiconfig_u_pkey |  | fdataid,fuseorgid |

---

## 系统集成配置-主表 t_pur_apiconfig

- **表名称：** 系统集成配置-主表
- **表名：** t_pur_apiconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 业务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fdisabledate | fdisabledate | timestamp | 0 |  |  | null |  |
| 4 | fissynsupgroup | 供应商分组 | bpchar | 1 |  | √ | ' ' | 供应商分组 |
| 5 | fissynorg | 组织 | bpchar | 1 |  | √ | ' ' | 组织 |
| 6 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fip | IP地址 | varchar | 100 |  | √ | ' ' | IP地址 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fissynproject | 项目 | bpchar | 1 |  | √ | ' ' | 项目 |
| 10 | fdbname | 数据中心 | varchar | 50 |  | √ | ' ' | 数据中心 |
| 11 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 12 | fissynunit | 计量单位 | bpchar | 1 |  | √ | ' ' | 计量单位 |
| 13 | fissynsupplier | 供应商 | bpchar | 1 |  | √ | ' ' | 供应商 |
| 14 | fissynsettype | 结算方式 | bpchar | 1 |  | √ | ' ' | 结算方式 |
| 15 | fname | fname | varchar | 100 |  | √ | ' ' |  |
| 16 | fissynuser | 用户 | bpchar | 1 |  | √ | ' ' | 用户 |
| 17 | fenablelog | 启用日志 | bpchar | 1 |  | √ | ' ' | 启用日志,枚举: 0 :禁用 1 :启用 |
| 18 | flanguage | 多语言 | bpchar | 1 |  | √ | ' ' | 多语言,枚举: 1 :繁体 2 :简体 3 :英文 |
| 19 | fissynwarehouse | 仓库 | bpchar | 1 |  | √ | ' ' | 仓库 |
| 20 | fdisablerid | fdisablerid | int8 | 64 |  | √ | 0 |  |
| 21 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 22 | fclient_id | 客户端ID | varchar | 50 |  | √ | ' ' | 客户端ID |
| 23 | fissynbizperson | 业务员 | bpchar | 1 |  | √ | ' ' | 业务员 |
| 24 | flicense | 认证(License) | varchar | 100 |  | √ | ' ' | 认证(License) |
| 25 | fport | 端口 | varchar | 50 |  | √ | ' ' | 端口 |
| 26 | fenable | 可用状态 | bpchar | 1 |  | √ | ' ' | 可用状态,枚举: 0 :禁用 1 :可用 |
| 27 | fnumber | 方案编码 | varchar | 50 |  | √ | ' ' | 方案编码 |
| 28 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 29 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 30 | fissynunitgroup | 计量单位组 | bpchar | 1 |  | √ | ' ' | 计量单位组 |
| 31 | fissynlot | 批号 | bpchar | 1 |  | √ | ' ' | 批号 |
| 32 | fissyncurrency | 币别 | bpchar | 1 |  | √ | ' ' | 币别 |
| 33 | fissynmaterial | 物料 | bpchar | 1 |  | √ | ' ' | 物料 |
| 34 | fpassword | 密码 | varchar | 50 |  | √ | ' ' | 密码 |
| 35 | fsystem | 对接系统 | bpchar | 1 |  | √ | ' ' | 对接系统,枚举: 1 :EAS 2 :票无忧 3 :快递100 4 :金蝶云平台 5 :苍穹供应链 6 :天眼查 7 :企查查 8 :大数据云平台 |
| 36 | fissyntrace | 跟踪号 | bpchar | 1 |  | √ | ' ' | 跟踪号 |
| 37 | fusername | 用户名 | varchar | 50 |  | √ | ' ' | 用户名 |
| 38 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :保存 B :已提交 C :已审核 |
| 39 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 40 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 41 | fislock | 启用锁 | bpchar | 1 |  | √ | ' ' | 启用锁,枚举: 0 :禁用 1 :启用 |
| 42 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 43 | ftid | 开票组织 | varchar | 50 |  | √ | ' ' | 开票组织 |
| 44 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 45 | fremark | fremark | varchar | 255 |  | √ | ' ' |  |
| 46 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 47 | fclient_secret | 客户端密匙 | varchar | 255 |  | √ | ' ' | 客户端密匙 |
| 48 | fissynmatgroup | 物料分组 | bpchar | 1 |  | √ | ' ' | 物料分组 |
| 49 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 50 | fctrlstrategy | 控制策略 | bpchar | 1 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 51 | fissynpaycond | 付款条件 | bpchar | 1 |  | √ | ' ' | 付款条件 |
| 52 | fissynbizgroup | 业务组 | bpchar | 1 |  | √ | ' ' | 业务组 |
| 53 | fenablecache | 启用缓存 | bpchar | 1 |  | √ | ' ' | 启用缓存,枚举: 0 :禁用 1 :启用 |
| 54 | fuseorgid | fuseorgid | int8 | 64 |  | √ | 0 |  |
| 55 | fissynlocation | 库位 | bpchar | 1 |  | √ | ' ' | 库位 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_pur_apiconfig_createorg |  | fcreateorgid |
| 2 | idx_pur_apiconfig_fmasterid |  | fmasterid |
| 3 | idx_pur_apiconfig_fnumber |  | fnumber |
| 4 | idx_t_pur_apiconfig_master |  | fmasterid |
| 5 | t_pur_apiconfig_pkey |  | fid |
