# 核销方案-cal_writeoffsolution

## 核销方案-多语言表 t_cal_writeoffsol_l

- **表名称：** 核销方案-多语言表
- **表名：** t_cal_writeoffsol_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 3 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cal_writeoffsol_l_pkey |  | fpkid |
| 2 | idx_cal_writeoffsol_l |  | fid,flocaleid |

---

## 单据体-子表 t_cal_writeoffsolentry

- **表名称：** 单据体-子表
- **表名：** t_cal_writeoffsolentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmatchruleid | 匹配规则 | int8 | 64 |  | √ | 0 | [匹配规则（旧） cal_matchrule](../sbs_files/cal_matchrule.md) |
| 3 | fbotpruleid | BOTP规则编码 | varchar | 36 |  | √ | ' ' | [转换规则 botp_crlist](../botp_files/botp_crlist.md) |
| 4 | fisflow | 流程方案 | bpchar | 1 |  | √ | ' ' | 流程方案 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cal_writeoffsolentry_pkey |  | fentryid |
| 2 | idx_cal_writeoffsolentry |  | fid |

---

## 核销方案-主表 t_cal_writeoffsol

- **表名称：** 核销方案-主表
- **表名：** t_cal_writeoffsol

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstatus | 数据状态 | varchar | 5 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fenable | 使用状态 | varchar | 5 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 8 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fwriteofftypeid | 核销类别 | int8 | 64 |  | √ | 0 | [核销类别（旧） cal_writeofftype](../sbs_files/cal_writeofftype.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cal_writeoffsol |  | fnumber |
| 2 | t_cal_writeoffsol_pkey |  | fid |
