# 工卡维护-mpdm_workcards

## 工卡维护-使用范围位图表 t_mpdm_workcards_m

- **表名称：** 工卡维护-使用范围位图表
- **表名：** t_mpdm_workcards_m

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
| 1 | pk_t_mpdm_workcards_m |  | forgid |

---

## 工卡维护-多语言表 t_mpdm_workcards_l

- **表名称：** 工卡维护-多语言表
- **表名：** t_mpdm_workcards_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 标题 | varchar | 255 |  | √ | ' ' | 标题 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 20 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mpdm_workcards_l |  | fpkid |
| 2 | index_mpdm_workcards_l |  | fid,flocaleid |

---

## 工卡维护-使用范围表 t_mpdm_workcards_u

- **表名称：** 工卡维护-使用范围表
- **表名：** t_mpdm_workcards_u

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
| 1 | idx_t_mpdm_workcards_u_uo |  | fuseorgid |
| 2 | pk_t_mpdm_workcards_u |  | fdataid,fuseorgid |

---

## 工卡维护-主表 t_mpdm_workcards

- **表名称：** 工卡维护-主表
- **表名：** t_mpdm_workcards

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdisableuserid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fzone | 功能位置 | int8 | 64 |  | √ | 0 | [功能位置 mpdm_functionlocation](../mpdm_files/mpdm_functionlocation.md) |
| 4 | fuseorg | fuseorg | int8 | 64 |  | √ | 0 |  |
| 5 | fdescribe | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fata | 章节号 | varchar | 50 |  | √ | ' ' | 章节号 |
| 8 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 9 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fworkcardtype | 工卡类型 | int8 | 64 |  | √ | 0 | [工卡类型 mpdm_jobcardtype](../mpdm_files/mpdm_jobcardtype.md) |
| 12 | fcardnumid | 工卡辅助识别码 | varchar | 80 |  | √ | ' ' | 工卡辅助识别码 |
| 13 | ftitle | 标题（废弃） | varchar | 255 |  | √ | ' ' | 标题（废弃） |
| 14 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 15 | fenddate | 有效期范围.结束 | timestamp | 0 |  |  | null | 有效期范围.结束 |
| 16 | fauxproperty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 17 | frefwordcard | 参考工卡号 | int8 | 64 |  | √ | 0 | [工卡维护 mpdm_workcards](../mpdm_files/mpdm_workcards.md) |
| 18 | fcardversion | 工卡版本号 | varchar | 50 |  | √ | ' ' | 工卡版本号 |
| 19 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 20 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 21 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 22 | fmaintrade | 主专业 | varchar | 36 |  | √ | ' ' | [树形基础资料模板 mpdm_professiona](../mpdm_files/mpdm_professiona.md) |
| 23 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 24 | fworkarea | 工作区域 | int8 | 64 |  | √ | 0 | [工作区域 mpdm_area](../mpdm_files/mpdm_area.md) |
| 25 | fmaterial | 产品编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 26 | fenableuserid | 启用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 27 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 28 | fname | 标题 | varchar | 255 |  | √ | ' ' | 标题 |
| 29 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 30 | fcustomer | 客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 31 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 32 | fspare | 需要物料 | bpchar | 1 |  | √ | '0' | 需要物料 |
| 33 | fenabledate | 启用时间 | timestamp | 0 |  |  | null | 启用时间 |
| 34 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 35 | fcardnum | 客户工卡号 | varchar | 80 |  | √ | ' ' | 客户工卡号 |
| 36 | ftool | 需要工具 | bpchar | 1 |  | √ | '0' | 需要工具 |
| 37 | fmaterialtype | 产品型号 | int8 | 64 |  | √ | 0 | [科目类型 bd_accounttype](../fibd_files/bd_accounttype.md) |
| 38 | fctrlstrategy | 控制策略 | varchar | 50 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 39 | fstartdate | 有效期范围.开始 | timestamp | 0 |  |  | null | 有效期范围.开始 |
| 40 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 41 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 42 | fworkstage | 工作类别 | int8 | 64 |  | √ | 0 | [工作类别 mpdm_workcategories](../mpdm_files/mpdm_workcategories.md) |
| 43 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |
| 44 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | index_mpdm_workcards_fcorgid |  | fcreateorgid |
| 2 | idx_t_mpdm_workcards_createorg |  | fcreateorgid |
| 3 | idx_t_mpdm_workcards_master |  | fmasterid |
| 4 | pk_t_mpdm_workcards |  | fid |
| 5 | index_mpdm_workcards_fctime |  | fcreatetime |
| 6 | index_mpdm_workcards_fnumber |  | fnumber |
