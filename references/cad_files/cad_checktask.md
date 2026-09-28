# 合法性检查任务-cad_checktask

## 单据体-子表 t_cad_checktaskentry

- **表名称：** 单据体-子表
- **表名：** t_cad_checktaskentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flevel | 告警级别 | bpchar | 1 |  | √ | ' ' | 告警级别,枚举: 1 :警告 2 :错误 |
| 3 | fisenable | 是否启用 | bpchar | 1 |  | √ | '1' | 是否启用 |
| 4 | fischange | 允许修改 | bpchar | 1 |  | √ | '1' | 允许修改 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fcheckitemid | 合法性检查项 | int8 | 64 |  | √ | 0 | 合法性检查项 cad_checkitem |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cad_checktaskentry |  | fentryid |
| 2 | idx_cad_checktaskentry |  | fid |

---

## 合法性检查任务-多语言表 t_cad_checktask_l

- **表名称：** 合法性检查任务-多语言表
- **表名：** t_cad_checktask_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fdescription | 描述 | varchar | 2000 |  | √ | ' ' | 描述 |
| 4 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cad_checktask_l |  | fid,flocaleid |
| 2 | pk_t_cad_checktask_l |  | fpkid |

---

## 合法性检查任务-主表 t_cad_checktask

- **表名称：** 合法性检查任务-主表
- **表名：** t_cad_checktask

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdescription | 描述 | varchar | 2000 |  | √ | ' ' | 描述 |
| 3 | fappnum | 所属应用 | varchar | 30 |  | √ | 'sca' | 所属应用,枚举: sca :标准成本 aca :实际成本 |
| 4 | fcaltype | 计算类型 | varchar | 80 |  | √ | ' ' | 计算类型,枚举: sca_finishcalwizards :完工产品结算 aca_terminalcalwizards :成本计算 sca_differencecalcwizards :差异分摊 sca_factcostreduction :实际成本还原 |
| 5 | fispreset | 是否预设 | bpchar | 1 |  | √ | '0' | 是否预设 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cad_checktask |  | fcaltype,fappnum |
| 2 | pk_t_cad_checktask |  | fid |
