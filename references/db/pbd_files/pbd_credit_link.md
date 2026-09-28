# 连接配置-pbd_credit_link

## 连接配置-使用范围表 t_pbd_link_u

- **表名称：** 连接配置-使用范围表
- **表名：** t_pbd_link_u

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
| 1 | pk_t_pbd_link_u |  | fdataid,fuseorgid |
| 2 | idx_t_pbd_link_u_uo |  | fuseorgid |

---

## 连接配置-多语言表 t_pbd_link_l

- **表名称：** 连接配置-多语言表
- **表名：** t_pbd_link_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
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
| 1 | pk_pbd_link_l |  | fpkid |
| 2 | idx_pbd_link_l_fid |  | fid |

---

## 适用组织配置-子表 t_pbd_link_orgentity

- **表名称：** 适用组织配置-子表
- **表名：** t_pbd_link_orgentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcompanyorg | 组织名称 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | fincludesuborg | 包含下级组织 | bpchar | 1 |  | √ | '0' | 包含下级组织 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pbd_link_orgentity |  | fentryid |
| 2 | idx_pbd_link_fid_fseq |  | fid,fseq |

---

## 连接配置-主表 t_pbd_link

- **表名称：** 连接配置-主表
- **表名：** t_pbd_link

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fwholegroup | 集团统一 | bpchar | 1 |  | √ | '1' | 集团统一 |
| 3 | fapplyorg | 适用组织范围 | varchar | 1000 |  | √ | ' ' | 适用组织范围 |
| 4 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | ftenantid | 租户 | varchar | 50 |  | √ | ' ' | 租户 |
| 6 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :保存 B :已提交 C :已审核 |
| 9 | fsyssourceid | 数据源 | int8 | 64 |  | √ | 0 | 数据源管理 isc_data_source |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 13 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 14 | fplatform | 平台 | int8 | 64 |  | √ | 0 | 外部系统 pbd_extsys |
| 15 | fopenstatus | 开通状态 | varchar | 50 |  | √ | ' ' | 开通状态,枚举: 1 :待开通 2 :运行中 3 :已停用 |
| 16 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 17 | fname | 方案名称 | varchar | 100 |  | √ | ' ' | 方案名称 |
| 18 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 19 | fclientid | ClientID/ID | varchar | 50 |  | √ | ' ' | ClientID/ID |
| 20 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 21 | fuser | 用户 | varchar | 100 |  | √ | ' ' | 用户 |
| 22 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 23 | fctrlstrategy | 控制策略 | varchar | 50 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 24 | fclientsecret | ClientSecret | varchar | 50 |  | √ | ' ' | ClientSecret |
| 25 | fpublickey | 客户公钥 | varchar | 500 |  | √ | ' ' | 客户公钥 |
| 26 | ftoken | 关联Token/Key | varchar | 50 |  | √ | ' ' | 关联Token/Key |
| 27 | fcallnums | 接口调用次数 | int8 | 64 |  | √ | 0 | 接口调用次数 |
| 28 | fenable | 可用状态 | bpchar | 1 |  | √ | '1' | 可用状态,枚举: 0 :禁用 1 :可用 |
| 29 | fjingweipublickey | 泾渭云公钥 | varchar | 500 |  | √ | ' ' | 泾渭云公钥 |
| 30 | fnumber | 方案编码 | varchar | 80 |  | √ | ' ' | 方案编码 |
| 31 | fuseorgid | 业务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 32 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |
| 33 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pbd_link_fmasterid |  | fmasterid |
| 2 | idx_t_pbd_link_master |  | fmasterid |
| 3 | idx_t_pbd_link_createorg |  | fcreateorgid |
| 4 | idx_pbd_link_fnumber |  | fnumber |
| 5 | pk_pbd_link |  | fid |
