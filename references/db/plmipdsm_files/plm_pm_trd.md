# 集成应用配置-plm_pm_trd

## 认证参数-子表 t_plm_pm_trd_auth

- **表名称：** 认证参数-子表
- **表名：** t_plm_pm_trd_auth

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fparam | 参数名 | varchar | 50 |  | √ | ' ' | 参数名 |
| 3 | fvalue | 参数值 | varchar | 500 |  | √ | ' ' | 参数值 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_pm_trd_auth_fk |  | fid |
| 2 | pk_plm_pm_trd_auth |  | fentryid |

---

## 集成应用配置-主表 t_plm_pm_trd

- **表名称：** 集成应用配置-主表
- **表名：** t_plm_pm_trd

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fname | 应用名称 | varchar | 50 |  | √ | ' ' | 应用名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fappsecret | 秘钥 | varchar | 50 |  | √ | ' ' | 秘钥 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fopenstyle | 打开方式 | varchar | 50 |  | √ | ' ' | 打开方式,枚举: A :iframe弹框 B :新页签 |
| 9 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 10 | fwidth | 弹框宽度 | numeric | 23 |  | √ | 960 | 弹框宽度 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fctrlstrategy | 控制策略 | varchar | 50 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 13 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 17 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 18 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 19 | furl | URL | varchar | 1000 |  | √ | ' ' | URL |
| 20 | fauthtype | 认证服务 | int8 | 64 |  | √ | 0 | 集成认证服务 plm_pm_trd_authtype |
| 21 | fheight | 弹框高度 | numeric | 23 |  | √ | 580 | 弹框高度 |
| 22 | fnumber | 应用编码 | varchar | 30 |  | √ | ' ' | 应用编码 |
| 23 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_plm_pm_trd_master |  | fmasterid |
| 2 | pk_plm_pm_trd |  | fid |
| 3 | idx_t_plm_pm_trd_createorg |  | fcreateorgid |

---

## 集成应用配置-使用范围表 t_plm_pm_trd_u

- **表名称：** 集成应用配置-使用范围表
- **表名：** t_plm_pm_trd_u

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
| 1 | idx_t_plm_pm_trd_u_uo |  | fuseorgid |
| 2 | pk_t_plm_pm_trd_u |  | fdataid,fuseorgid |

---

## 集成应用配置-多语言表 t_plm_pm_trd_l

- **表名称：** 集成应用配置-多语言表
- **表名：** t_plm_pm_trd_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 应用名称 | varchar | 50 |  | √ | ' ' | 应用名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_pm_trd_l_0 |  | fid,flocaleid |
| 2 | pk_plm_pm_trd_l |  | fpkid |
