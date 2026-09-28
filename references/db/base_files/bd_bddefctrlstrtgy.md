# 受控基础资料-bd_bddefctrlstrtgy

## 受控基础资料-主表 t_bd_defaultctrlstrategy

- **表名称：** 受控基础资料-主表
- **表名：** t_bd_defaultctrlstrategy

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdefaultctrlstrategy | 默认控制策略 | varchar | 10 |  | √ | ' ' | 默认控制策略,枚举: 5 :全局共享 7 :私有 1 :逐级分配 2 :分配/局部共享 6 :管控范围内共享 |
| 3 | fxkplmplugin | PLM插件 | varchar | 150 |  | √ | ' ' | PLM插件 |
| 4 | fsolidifyobj | 固化关系对象 | varchar | 50 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 5 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 6 | fmasteridfieldname | masterid字段名 | varchar | 20 |  | √ | 'fmasterid' | masterid字段名 |
| 7 | fxkcancelassign | 取消分配状态校验 | bpchar | 1 |  | √ | '1' | 取消分配状态校验 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fappsystemid | 应用系统 | varchar | 36 |  | √ | ' ' | 业务应用实体 bos_devportal_bizapp |
| 10 | fstatus | 数据状态 | varchar | 10 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fxklock | 是否锁定 | bpchar | 1 |  | √ | '0' | 是否锁定 |
| 14 | fenablesolidify | 启用分表 | bpchar | 1 |  | √ | '0' | 启用分表 |
| 15 | fissystem | 系统预设 | bpchar | 1 |  | √ | null | 系统预设,枚举: 1 :是 0 :否 |
| 16 | fmasteridpropname | masterid属性名 | varchar | 20 |  | √ | 'masterid' | masterid属性名 |
| 17 | fissyncdata | 同步数据 | bpchar | 1 |  | √ | '0' | 同步数据 |
| 18 | fplugin | 插件 | varchar | 100 |  | √ | ' ' | 插件 |
| 19 | fassignundetail | 允许分配非明细 | bpchar | 1 |  | √ | '0' | 允许分配非明细 |
| 20 | fupgradestatus | 模型状态 | varchar | 30 |  | √ | '1' | 模型状态,枚举: 1 :未升级 2 :已升级 |
| 21 | fxkallocationtypes | 可分配类型 | varchar | 50 |  | √ | '1' | 可分配类型,枚举: 1 :分配 2 :局部共享 |
| 22 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 23 | fdefaultmanagestrategy | 默认管理策略 | varchar | 10 |  | √ | ' ' | 默认管理策略,枚举: 1 :创建组织管理 0 :管理组织管理 |
| 24 | fbasedataid | 基础资料 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 25 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 26 | fxkshowallocationtypes | 分配方式 | varchar | 50 |  | √ | ' ' | 分配方式,枚举: 1 :分配 2 :局部共享 |
| 27 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 28 | fctrlview | 控制视图 | int8 | 64 |  | √ | 0 | 组织视图方案 bos_org_viewschema |
| 29 | fcontrolrule | 是否自定义控制规则 | bpchar | 1 |  | √ | '0' | 是否自定义控制规则 |
| 30 | fxkassignedopt | 分配后操作 | varchar | 30 |  | √ | ' ' | 分配后操作,枚举: assigned_save :保存 assigned_submit :提交 assigned_check :审核 |
| 31 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 32 | fislockview | 控制视图锁定 | bpchar | 1 |  | √ | '0' | 控制视图锁定 |
| 33 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 34 | fdatatype | 资料类型 | varchar | 10 |  | √ | ' ' | 资料类型,枚举: 1 :是 2 :业务基础数据 |
| 35 | fcheckstatus | 模型检查状态 | bpchar | 1 |  | √ | '1' | 模型检查状态 |
| 36 | fsolidifystatus | 固化状态 | bpchar | 1 |  | √ | '0' | 固化状态 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_defaultctrlstrategy_bd |  | fbasedataid |
| 2 | t_bd_defaultctrlstrategy_pkey |  | fid |

---

## 受控基础资料-多语言表 t_bd_defaultctrlstrategy_l

- **表名称：** 受控基础资料-多语言表
- **表名：** t_bd_defaultctrlstrategy_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_defaultctrlstrategy_l_id |  | fid,flocaleid |
| 2 | t_bd_defaultctrlstrategy_l_pkey |  | fpkid |
