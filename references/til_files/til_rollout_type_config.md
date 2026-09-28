# 进项转出映射配置-til_rollout_type_config

## 进项转出映射配置-主表 t_til_rollout_type_config

- **表名称：** 进项转出映射配置-主表
- **表名：** t_til_rollout_type_config

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fmapbill | 映射单据 | varchar | 50 |  | √ | ' ' | 映射单据,枚举: jxzcfpdj :进项转出发票登记 |
| 4 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 5 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | fgroupid | 分组 | int8 | 64 |  | √ | 0 | 业务定义分录 tpo_tcvat_bizdef_entity |
| 7 | foutputtype | 进项转出类型 | varchar | 50 |  | √ | ' ' | 进项转出类型,枚举: 2 :免税项目用 3 :集体福利、个人消费 4 :非正常损失 5 :简易计税方法征税项目用 6 :免抵退税办法不得抵扣的进项税额 8 :异常凭证转出进项税额 11 :其他 |
| 8 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 10 | fmapfield | 映射字段 | varchar | 50 |  | √ | ' ' | 映射字段,枚举: zcyy :转出原因 |
| 11 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fctrlstrategy | 控制策略 | varchar | 50 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 14 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 17 | fsysdata | 系统预设 | varchar | 50 |  | √ | ' ' | 系统预设,枚举: yes :是 no :否 |
| 18 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 19 | fmapvalue | 映射名称 | varchar | 50 |  | √ | ' ' | 映射名称 |
| 20 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 21 | fenable | 状态 | varchar | 50 |  | √ | ' ' | 状态,枚举: 0 :禁用 1 :可用 |
| 22 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 23 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_til_rollout_type_config |  | fid |
| 2 | idx_t_til_rollout_type_config_master |  | fmasterid |
| 3 | idx_t_til_rollout_type_config_createorg |  | fcreateorgid |

---

## 进项转出映射配置-使用范围位图表 t_til_rollout_type_config_m

- **表名称：** 进项转出映射配置-使用范围位图表
- **表名：** t_til_rollout_type_config_m

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
| 1 | pk_t_til_rollout_type_config_m |  | forgid |

---

## 进项转出映射配置-多语言表 t_til_rollout_type_config_l

- **表名称：** 进项转出映射配置-多语言表
- **表名：** t_til_rollout_type_config_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_til_rollout_type_config_l |  | fpkid |

---

## 进项转出映射配置-使用范围表 t_til_rollout_type_config_u

- **表名称：** 进项转出映射配置-使用范围表
- **表名：** t_til_rollout_type_config_u

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
| 1 | idx_t_til_rollout_type_config_u_uo |  | fuseorgid |
| 2 | pk_t_til_rollout_type_config_u |  | fdataid,fuseorgid |
