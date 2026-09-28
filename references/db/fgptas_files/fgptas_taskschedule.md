# 财务报告生成定时方案-fgptas_taskschedule

## 财务报告生成定时方案-多语言表 t_fgptas_taskschedule_l

- **表名称：** 财务报告生成定时方案-多语言表
- **表名：** t_fgptas_taskschedule_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 方案名称 | varchar | 255 |  | √ | ' ' | 方案名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fgptas_taskschedule_l_0 |  | fid,flocaleid |
| 2 | pk_fgptas_taskschedule_l |  | fpkid |

---

## 财务报告生成定时方案-主表 t_fgptas_taskschedule

- **表名称：** 财务报告生成定时方案-主表
- **表名：** t_fgptas_taskschedule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fscheduleplan | 调度计划 | varchar | 1024 |  | √ | ' ' | 调度计划 |
| 2 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 3 | fautogenfunc | 自动生成方式 | varchar | 50 |  | √ | ' ' | 自动生成方式,枚举: 1 :定时生成 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fname | 方案名称 | varchar | 255 |  | √ | ' ' | 方案名称 |
| 6 | fscheduleplaninfoid | 调度计划信息id | varchar | 255 |  | √ | ' ' | 调度计划信息id |
| 7 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 8 | fmodifytime | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 9 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fexecutor | 执行人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fenable | 使用状态 | bpchar | 1 |  | √ | 0 | 使用状态,枚举: 0 :禁用 1 :可用 |
| 14 | fnumber | 方案编号 | varchar | 18 |  | √ | ' ' | 方案编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fgptas_taskschedule |  | fid |
| 2 | idx_fgptas_taskschedule_m0 |  | fmasterid |

---

## 报告模板-子表 t_fgptas_taskreporttmpl

- **表名称：** 报告模板-子表
- **表名：** t_fgptas_taskreporttmpl

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | freporttmpl | 报告模板 | int8 | 64 |  | √ | 0 | [财务报告模板 fgptas_fireporttemplate](../fgptas_files/fgptas_fireporttemplate.md) |
| 3 | fperiod | 期间 | varchar | 50 |  | √ | ' ' | 期间,枚举: 1 :当前期间的上一期 |
| 4 | fcycletype | 周期类型 | varchar | 50 |  | √ | ' ' | 周期类型,枚举: 2 :日报 4 :月报 5 :季报 6 :半年报 7 :年报 |
| 5 | fdate | 日期 | timestamp | 0 |  |  | null | 日期 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fenabled | 启用 | bpchar | 1 |  | √ | '1' | 启用 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fgendocumenttype | 生成文档类型 | varchar | 50 |  | √ | ' ' | 生成文档类型,枚举: 1 :Word 2 :PPT |
| 10 | fscopeid | 合并范围 | int8 | 64 |  | √ | 0 | [合并范围 xkcr_scope](../xkcr_files/xkcr_scope.md) |
| 11 | faccountbook | 账簿 | int8 | 64 |  | √ | 0 | [账簿 gl_accountbook](../gl_files/gl_accountbook.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fgptas_taskreporttmpl |  | fentryid |
| 2 | idx_fgptas_taskreporttmpl_fk |  | fid |
