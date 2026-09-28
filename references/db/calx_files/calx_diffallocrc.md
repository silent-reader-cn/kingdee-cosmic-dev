# 差异分摊记录-calx_diffallocrc

## 差异分摊记录-主表 t_cal_diffallocrc

- **表名称：** 差异分摊记录-主表
- **表名：** t_cal_diffallocrc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftime | 耗时（秒） | int8 | 64 |  | √ | 0 | 耗时（秒） |
| 3 | fstatus | 状态 | bpchar | 1 |  | √ | ' ' | 状态,枚举: A :处理中 B :成功 C :失败 |
| 4 | fparam | 向导参数 | varchar | 255 |  | √ | ' ' | 向导参数 |
| 5 | fallocmodel | 分摊方式 | varchar | 30 |  | √ | ' ' | 分摊方式,枚举: A :按单据编号 B :按单据类型 |
| 6 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | fuserid | 操作用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | foperation | 操作 | varchar | 50 |  | √ | ' ' | 操作 |
| 11 | fparam_tag | 向导参数_详情 | text | 0 |  |  | null | 向导参数_详情 |
| 12 | fstarttime | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cal_diffallocrc |  | fid |
| 2 | idx_cal_diffallocrc_st |  | fstarttime |
| 3 | idx_cal_diffallocrc_user |  | fuserid |

---

## 差异分摊记录-多语言表 t_cal_diffallocrc_l

- **表名称：** 差异分摊记录-多语言表
- **表名：** t_cal_diffallocrc_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | foperation | 操作 | varchar | 80 |  | √ | ' ' | 操作 |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cal_diffallocrc_l |  | fpkid |
| 2 | idx_cal_diffallocrc_l |  | fid,flocaleid |

---

## 描述-子表 t_cal_diffallocrcentry

- **表名称：** 描述-子表
- **表名：** t_cal_diffallocrcentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 3 | fdesc | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cal_ddiffallocrcentry_id |  | fid |
| 2 | pk_cal_diffallocrcentry |  | fentryid |
