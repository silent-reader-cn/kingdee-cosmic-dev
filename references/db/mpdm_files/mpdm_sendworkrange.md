# 派工范围-mpdm_sendworkrange

## 单据体-子表 t_mpdm_sendworkrangeentry

- **表名称：** 单据体-子表
- **表名：** t_mpdm_sendworkrangeentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fuserid | 工号 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | fmftteamid | 团队编码 | int8 | 64 |  | √ | 0 | [制造团队 mpdm_mftteam](../mpdm_files/mpdm_mftteam.md) |
| 6 | fequipmentid | 设备编码 | int8 | 64 |  | √ | 0 | [设备 sfc_equipment](../mpdm_files/sfc_equipment.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpdm_sendworkrangeentry |  | fentryid |
| 2 | idx_mpdm_swrentry_fid |  | fid |

---

## 派工范围-主表 t_mpdm_sendworkrange

- **表名称：** 派工范围-主表
- **表名：** t_mpdm_sendworkrange

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsendworkbatchtype | 派工批量类型 | bpchar | 1 |  | √ | ' ' | 派工批量类型,枚举: A :整单 B :工序基本批量 C :自定义批量 |
| 3 | fjobtype | 作业类型 | bpchar | 1 |  | √ | ' ' | 作业类型,枚举: B :个人作业 A :团队作业 |
| 4 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fsendworkmode | 派工方式 | bpchar | 1 |  | √ | ' ' | 派工方式,枚举: A :自动 B :手动 |
| 6 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fdisableuser | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | faudittime | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fdisabletime | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 11 | fsendworktype | 派工对象类型 | bpchar | 1 |  | √ | ' ' | 派工对象类型,枚举: A :设备 B :人员 C :团队 |
| 12 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fauditor | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fworkcenterid | 工作中心 | int8 | 64 |  | √ | 0 | [工作中心 sfc_workcenter](../mpdm_files/sfc_workcenter.md) |
| 17 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 18 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 19 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 20 | fname | 名称 | varchar | 500 |  | √ | ' ' | 名称 |
| 21 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 22 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 23 | fctrlstrategy | 控制策略 | varchar | 5 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 24 | fenabletime | 启用时间 | timestamp | 0 |  |  | null | 启用时间 |
| 25 | fenableuser | 启用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 26 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 27 | fnumber | 编码 | varchar | 140 |  | √ | ' ' | 编码 |
| 28 | fuseorgid | fuseorgid | int8 | 64 |  | √ | 0 |  |
| 29 | fsendworkbatch | 派工批量 | numeric | 23 | 10 | √ | 0 | 派工批量 |
| 30 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_mpdm_sendworkrange_master |  | fmasterid |
| 2 | pk_mpdm_sendworkrange |  | fid |
| 3 | idx_t_mpdm_sendworkrange_createorg |  | fcreateorgid |
| 4 | idx_mpdm_sendworkrange_center |  | fworkcenterid |

---

## 派工范围-多语言表 t_mpdm_sendworkrange_l

- **表名称：** 派工范围-多语言表
- **表名：** t_mpdm_sendworkrange_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 500 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | 'zh_CN' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpdm_sendworkrange_l |  | fpkid |
| 2 | idx_mpdm_sendworkrange_l_fid |  | fid,flocaleid |

---

## 派工范围-使用范围表 t_mpdm_sendworkrange_u

- **表名称：** 派工范围-使用范围表
- **表名：** t_mpdm_sendworkrange_u

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
| 1 | idx_t_mpdm_sendworkrange_u_uo |  | fuseorgid |
| 2 | pk_t_mpdm_sendworkrange_u |  | fdataid,fuseorgid |
