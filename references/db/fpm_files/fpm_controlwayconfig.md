# 控制策略设置（废弃）-fpm_controlwayconfig

## 控制策略设置（废弃）-多语言表 t_fpm_controlwayconfig_l

- **表名称：** 控制策略设置（废弃）-多语言表
- **表名：** t_fpm_controlwayconfig_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 策略名称 | varchar | 50 |  | √ | ' ' | 策略名称 |
| 3 | fcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 4 | flocaleid | flocaleid | varchar | 50 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fpm_controlwayconfig_l |  | fpkid |
| 2 | idx_fpm_controlwayconfig_l |  | fid |

---

## 树形单据体-子表 t_fpm_control_strategy

- **表名称：** 树形单据体-子表
- **表名：** t_fpm_control_strategy

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcontrolintensity | 控制强度 | varchar | 50 |  | √ | ' ' | 控制强度,枚举: Rigid :刚性 Soft :柔性 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 | pid |
| 5 | fdetailcontrol | 按明细项控制 | bpchar | 1 |  | √ | ' ' | 按明细项控制 |
| 6 | fdetailcontrolbasis | 明细项控制依据 | varchar | 1024 |  | √ | ' ' | 明细项控制依据,枚举: |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fsubjectid | 计划科目编码 | int8 | 64 |  | √ | 0 | [维度成员模板（废弃） fpm_member](../fpm_files/fpm_member.md) |
| 9 | fsubjectflow | 计划科目流向 | varchar | 50 |  | √ | ' ' | 计划科目流向,枚举: A :余额 B :流入 C :流出 D :不限 E :净流入 |
| 10 | fcontrolcoefficient | 控制系数（%） | numeric | 5 | 2 | √ | 0 | 控制系数（%） |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fpm_control_strategy |  | fentryid |
| 2 | idx_fpm_control_startegy_fid |  | fid |

---

## 单据体-子表 t_fpm_apply_reportorg

- **表名称：** 单据体-子表
- **表名：** t_fpm_apply_reportorg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | freportorgid | 编报主体编码 | int8 | 64 |  | √ | 0 | [维度成员模板（废弃） fpm_member](../fpm_files/fpm_member.md) |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fpm_apply_reportorg |  | fentryid |
| 2 | idx_fpm_apply_reportorg_fid |  | fid |

---

## 控制策略设置（废弃）-主表 t_fpm_controlwayconfig

- **表名称：** 控制策略设置（废弃）-主表
- **表名：** t_fpm_controlwayconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 最后更新人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | fperiodstrategy | 期间控制策略 | varchar | 50 |  | √ | ' ' | 期间控制策略,枚举: CurrentControl :当期控制 DetailPeriodControl :按明细期间控制 |
| 5 | fenabledate | 启用日期 | timestamp | 0 |  |  | null | 启用日期 |
| 6 | fdisabledate | 禁用日期 | timestamp | 0 |  |  | null | 禁用日期 |
| 7 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fbodysysid | 体系 | int8 | 64 |  | √ | 0 | [体系管理1（废弃） fpm_bodysysmanage](../fpm_files/fpm_bodysysmanage.md) |
| 9 | fmodifytime | 最后更新时间 | timestamp | 0 |  |  | null | 最后更新时间 |
| 10 | fcontrolwarnnode | 额度控制及提醒节点 | varchar | 50 |  | √ | ' ' | 额度控制及提醒节点,枚举: Preempted :预占 |
| 11 | fstatus | 数据状态 | bpchar | 5 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | funavailablewarn | 可用额度不足预警提示线（%） | int4 | 32 |  | √ | 0 | 可用额度不足预警提示线（%） |
| 15 | freporttype | freporttype | int8 | 64 |  | √ | 0 |  |
| 16 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 17 | fenablerid | 启用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fpm_controlwayconfig |  | fid |
| 2 | idx_fpm_controlway |  | fnumber |
| 3 | idx_fpm_bodysys |  | fbodysysid |

---

## 受控编报类型-多选基础资料表 t_fpm_controlreporttype

- **表名称：** 受控编报类型-多选基础资料表
- **表名：** t_fpm_controlreporttype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [编报类型设置（废弃） fpm_orgreporttype](../fpm_files/fpm_orgreporttype.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fpm_controlreporttype |  | fid |
| 2 | pk_t_fpm_controlreporttype |  | fpkid |
