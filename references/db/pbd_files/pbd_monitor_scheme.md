# 风险监控方案-pbd_monitor_scheme

## 检查项单据体-子表 t_pbd_monitcheckitementry

- **表名称：** 检查项单据体-子表
- **表名：** t_pbd_monitcheckitementry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fcheckitemid | 检查项 | int8 | 64 |  | √ | 0 | [检查项 pbd_check_item](../pbd_files/pbd_check_item.md) |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pbd_monitcheckitemen_fid |  | fid |
| 2 | pk_pbd_monitcheckitementry |  | fentryid |

---

## 卡片组件-多选基础资料表 t_pbd_monitorscheme_card

- **表名称：** 卡片组件-多选基础资料表
- **表名：** t_pbd_monitorscheme_card

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [卡片组件 pbd_cardcomp](../pbd_files/pbd_cardcomp.md) |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pbd_monitorscheme_card_ent |  | fentryid |
| 2 | pk_pbd_monitorscheme_card |  | fpkid |

---

## 风险监控方案-主表 t_pbd_monitorscheme

- **表名称：** 风险监控方案-主表
- **表名：** t_pbd_monitorscheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ffiltergridtext | 过滤条件 | varchar | 2000 |  | √ | ' ' | 过滤条件 |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | fmonitortype | 监控方式 | bpchar | 1 |  | √ | ' ' | 监控方式,枚举: 1 :操作触发 2 :定期监控 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 10 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 11 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 12 | fexceplan | 调度计划id | varchar | 50 |  | √ | ' ' | 调度计划id |
| 13 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 14 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 15 | fname | 方案名称 | varchar | 255 |  | √ | ' ' | 方案名称 |
| 16 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 18 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 19 | fctrlstrategy | 控制策略 | varchar | 50 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 20 | ffiltergridtext_tag | 过滤条件_详情 | text | 0 |  |  | null | 过滤条件_详情 |
| 21 | fbizobjectid | 监控对象 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 22 | fissys | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 23 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 24 | fexceplandesc | 执行计划 | varchar | 2000 |  | √ | ' ' | 执行计划 |
| 25 | fnumber | 方案编码 | varchar | 80 |  | √ | ' ' | 方案编码 |
| 26 | fdimid | 监控维度 | int8 | 64 |  | √ | 0 | [分析维度 pbd_dim](../pbd_files/pbd_dim.md) |
| 27 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |
| 28 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_pbd_monitorscheme_master |  | fmasterid |
| 2 | pk_pbd_monitorscheme |  | fid |
| 3 | idx_pbd_monitorscheme_fnumber |  | fnumber |
| 4 | idx_t_pbd_monitorscheme_createorg |  | fcreateorgid |

---

## 风险监控方案-使用范围表 t_pbd_monitorscheme_u

- **表名称：** 风险监控方案-使用范围表
- **表名：** t_pbd_monitorscheme_u

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
| 1 | idx_t_pbd_monitorscheme_u_uo |  | fuseorgid |
| 2 | pk_t_pbd_monitorscheme_u |  | fdataid,fuseorgid |

---

## 风险监控方案-多语言表 t_pbd_monitorscheme_l

- **表名称：** 风险监控方案-多语言表
- **表名：** t_pbd_monitorscheme_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | fremark | varchar | 512 |  | √ | ' ' |  |
| 3 | fname | 方案名称 | varchar | 255 |  | √ | ' ' | 方案名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pbd_monitorscheme_l |  | fpkid |
| 2 | idx_pbd_monitorscheme_l_fid |  | fid,flocaleid |
