# 变更条件-pds_chgcondition

## 变更条件-多语言表 t_pds_chgcondition_l

- **表名称：** 变更条件-多语言表
- **表名：** t_pds_chgcondition_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 600 |  | √ | ' ' | 备注 |
| 3 | fname | 名称 | varchar | 300 |  | √ | ' ' | 名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pds_chgcondition_l_fname |  | fname |
| 2 | pk_pds_chgcondition_l |  | fpkid |
| 3 | idx_pds_chgcondition_l_fid |  | fid,flocaleid |

---

## 变更条件-主表 t_pds_chgcondition

- **表名称：** 变更条件-主表
- **表名：** t_pds_chgcondition

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 600 |  | √ | ' ' | 备注 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fname | 名称 | varchar | 300 |  | √ | ' ' | 名称 |
| 5 | fbiznodeid | 业务节点 | int8 | 64 |  | √ | 0 | 业务节点 pds_biznode |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fchgtypeid | 变更类型 | int8 | 64 |  | √ | 0 | 组件模板配置 pds_tplconfig |
| 12 | fsourcetypeid | 适用的寻源流程 | int8 | 64 |  | √ | 0 | 流程配置 pds_flowconfig |
| 13 | fisforbidden | 是否允许禁用 | bpchar | 1 |  | √ | '0' | 是否允许禁用 |
| 14 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 15 | fplugin | 变更判断插件 | varchar | 100 |  | √ | ' ' | 变更判断插件 |
| 16 | fnumber | 执行顺序 | varchar | 30 |  | √ | ' ' | 执行顺序 |
| 17 | fissyspreset | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pds_chg_fbiznodeid |  | fbiznodeid |
| 2 | pk_pds_chgcondition |  | fid |
| 3 | idx_pds_chg_fnumber |  | fnumber |
| 4 | idx_pds_chg_fsourcetypeid |  | fsourcetypeid |
| 5 | idx_pds_chg_fchgtypeid |  | fchgtypeid |
| 6 | idx_pds_chg_fcreatetime |  | fcreatetime |
