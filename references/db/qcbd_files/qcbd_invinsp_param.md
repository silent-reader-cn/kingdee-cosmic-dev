# 库存检验参数-qcbd_invinsp_param

## 库存检验参数-主表 t_qcbd_inspparam

- **表名称：** 库存检验参数-主表
- **表名：** t_qcbd_inspparam

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fisbadtoinitial_sg | 不良品处理单反审核回初始库存状态 | bpchar | 1 |  | √ | '0' | 不良品处理单反审核回初始库存状态 |
| 3 | finvstatus_sgid | 请检自动转换库存状态 | int8 | 64 |  | √ | 0 | 库存状态 bd_invstatus |
| 4 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | ffreezestatusid | 质检冻结库存状态 | int8 | 64 |  | √ | 0 | 库存状态 bd_invstatus |
| 6 | fisbadtoinitial | 不良品处理单反审核回初始库存状态 | bpchar | 1 |  | √ | '0' | 不良品处理单反审核回初始库存状态 |
| 7 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fdisqualifiedstatusid | 不合格品库存状态 | int8 | 64 |  | √ | 0 | 库存状态 bd_invstatus |
| 9 | fisfrezz_sg | 请检冻结库存（废弃） | bpchar | 1 |  | √ | '0' | 请检冻结库存（废弃） |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | finvstatusid | 请检自动转换库存状态 | int8 | 64 |  | √ | 0 | 库存状态 bd_invstatus |
| 12 | fstatus | 数据状态 | varchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fbusinessorgid | 业务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 16 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 17 | ffreezstatus_sg | 质检冻结库存状态 | int8 | 64 |  | √ | 0 | 库存状态 bd_invstatus |
| 18 | fisinsptoinitial_sg | 检验单反审核自动回初始库存状态 | bpchar | 1 |  | √ | '0' | 检验单反审核自动回初始库存状态 |
| 19 | fqualifiedstatusid | 合格品目标库存状态 | int8 | 64 |  | √ | 0 | 库存状态 bd_invstatus |
| 20 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 21 | fquastatus_sg | 合格品目标库存状态 | int8 | 64 |  | √ | 0 | 库存状态 bd_invstatus |
| 22 | fisallowcrounaudit | 允许跨月单据反审核 | bpchar | 1 |  | √ | '0' | 允许跨月单据反审核 |
| 23 | finventoryorgid | finventoryorgid | int8 | 64 |  | √ | 0 |  |
| 24 | fxkallocationtype | 分配类型 | varchar | 30 |  | √ | ' ' | 分配类型,枚举: 1 :个性化 2 :共享型 |
| 25 | fisfrezzinventory | 请检冻结库存·（废弃） | bpchar | 1 |  | √ | '0' | 请检冻结库存·（废弃） |
| 26 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 27 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 28 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 29 | fisinsptoinitial | 检验单反审核自动回初始库存状态 | bpchar | 1 |  | √ | '0' | 检验单反审核自动回初始库存状态 |
| 30 | fdisqualstatus_sg | 不合格品库存状态 | int8 | 64 |  | √ | 0 | 库存状态 bd_invstatus |
| 31 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 32 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 33 | ffreezetime_sg | 请检冻结触发时机（废弃） | varchar | 1 |  | √ | 'A' | 请检冻结触发时机（废弃）,枚举: B :提交 C :审核 |
| 34 | finvautoexchange | 检验自动形态转换 | bpchar | 1 |  | √ | '1' | 检验自动形态转换 |
| 35 | fautoexchange | 检验自动形态转换 | bpchar | 1 |  | √ | '1' | 检验自动形态转换 |
| 36 | fctrlstrategy | 控制策略 | varchar | 1 |  | √ | '5' | 控制策略,枚举: 2 :分配/局部共享 1 :逐级分配 5 :全局共享 6 :管控范围内共享 7 :私有 |
| 37 | fisallowcrounaudit_sg | 允许跨月单据反审核 | bpchar | 1 |  | √ | '0' | 允许跨月单据反审核 |
| 38 | ffreezetime | 请检冻结触发时机（废弃） | varchar | 1 |  | √ | 'A' | 请检冻结触发时机（废弃）,枚举: B :提交 C :审核 |
| 39 | fenable | 使用状态 | varchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 40 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 41 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 42 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_qcbd_inspparamid |  | fid |
| 2 | idx_t_qcbd_inspparam_master |  | fmasterid |
| 3 | idx_t_qcbd_inspparam_createorg |  | fcreateorgid |
| 4 | uidx_qcbd_inspparam_billno |  | fnumber |

---

## 配置信息-子表 t_qcbd_inspconfentry

- **表名称：** 配置信息-子表
- **表名：** t_qcbd_inspconfentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fprocessmodeid | 不良品处理方式 | int8 | 64 |  | √ | 0 | 不良品处理方式 bd_badhandmode |
| 4 | finventorystatusid | 目标库存状态 | int8 | 64 |  | √ | 0 | 库存状态 bd_invstatus |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_qcbd_inspentryid |  | fentryid |

---

## 库存组织-多选基础资料表 t_qcbd_inspparam_org

- **表名称：** 库存组织-多选基础资料表
- **表名：** t_qcbd_inspparam_org

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_qcbd_inspamorg_pk |  | fpkid |

---

## 库存检验参数-多语言表 t_qcbd_inspparam_l

- **表名称：** 库存检验参数-多语言表
- **表名：** t_qcbd_inspparam_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 255 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 255 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_qcbd_inspparam_lpk |  | fpkid |

---

## 库存检验参数-使用范围表 t_qcbd_inspparam_u

- **表名称：** 库存检验参数-使用范围表
- **表名：** t_qcbd_inspparam_u

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
| 1 | pk_t_qcbd_inspparam_u |  | fdataid,fuseorgid |
| 2 | idx_t_qcbd_inspparam_u_uo |  | fuseorgid |
