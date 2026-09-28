# 自动对账方案-frm_autoreconciliation

## 自动对账方案-主表 t_frm_autoreconciliation

- **表名称：** 自动对账方案-主表
- **表名：** t_frm_autoreconciliation

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fstopstarttime | 终止执行时间.开始 | int4 | 32 |  | √ | 0 | 终止执行时间.开始 |
| 7 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fsheduleplanid | 调度计划id | varchar | 50 |  | √ | ' ' | 调度计划id |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fexecutor | 执行人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | ffailretrystrategy | 重试策略 | varchar | 50 |  | √ | ' ' | 重试策略,枚举: ignore :直接挂起 tryagain :重试一次 tryagainthree :重试三次 |
| 13 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 14 | fexceplandesc | 调度计划 | varchar | 510 |  | √ | ' ' | 调度计划 |
| 15 | fnumber | 方案编码 | varchar | 30 |  | √ | ' ' | 方案编码 |
| 16 | fstopendtime | 终止执行时间.结束 | int4 | 32 |  | √ | 0 | 终止执行时间.结束 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_frm_autorecon_create |  | fcreatetime |
| 2 | pk_frm_autoreconciliation |  | fid |

---

## 单据体-子表 t_frm_autoreconentry

- **表名称：** 单据体-子表
- **表名：** t_frm_autoreconentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcheckperiodid | 对账期间id | int8 | 64 |  | √ | 0 | 对账期间id |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | facctbook | 账簿 | int8 | 64 |  | √ | 0 | [账簿 gl_accountbook](../gl_files/gl_accountbook.md) |
| 6 | fentryenable | 启用 | bpchar | 1 |  | √ | '1' | 启用 |
| 7 | fcheckperiodname | 对账期间 | varchar | 255 |  | √ | ' ' | 对账期间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_frm_autoreconentry |  | fentryid |
| 2 | idx_frm_autoreconentry_fid |  | fid |

---

## 业务系统-多选基础资料表 t_frm_autoreconentry_app

- **表名称：** 业务系统-多选基础资料表
- **表名：** t_frm_autoreconentry_app

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | varchar | 36 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_frm_autoreconentry_app |  | fpkid |
| 2 | idx_frm_autoreconentry_app |  | fentryid |

---

## 自动对账方案-多语言表 t_frm_autoreconciliation_l

- **表名称：** 自动对账方案-多语言表
- **表名：** t_frm_autoreconciliation_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fexceplanlang | 执行计划多语言 | varchar | 255 |  | √ | ' ' | 执行计划多语言 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_frm_autoreconciliation_l |  | fpkid |
| 2 | idx_frm_autorecon_l |  | fid,flocaleid |
