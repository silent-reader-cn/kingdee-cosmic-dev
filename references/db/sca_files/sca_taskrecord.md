# 任务记录-sca_taskrecord

## 单据体-子表 t_sca_taskrecordentry

- **表名称：** 单据体-子表
- **表名：** t_sca_taskrecordentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fsubtime | 耗时（毫秒） | int8 | 64 |  | √ | 0 | 耗时（毫秒） |
| 4 | fsubparam | 子页面参数 | varchar | 255 |  | √ | ' ' | 子页面参数 |
| 5 | fdetailconfigid | 明细配置ID | int8 | 64 |  | √ | 0 | 明细配置ID |
| 6 | fsubname | 任务明细 | varchar | 255 |  | √ | ' ' | 任务明细 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fsubparam_tag | 子页面参数_详情 | text | 0 |  |  | null | 子页面参数_详情 |
| 9 | fdetail | 执行详情 | varchar | 255 |  | √ | ' ' | 执行详情 |
| 10 | fsubnextentity | 子页面 | varchar | 50 |  | √ | ' ' | 子页面 |
| 11 | fsubstatus | 状态 | varchar | 30 |  | √ | ' ' | 状态,枚举: 1 :未执行 2 :执行中 3 :失败 4 :成功 7 :警告 |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 13 | fsubstarttime | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_sca_taskrecordentry_pkey |  | fentryid |
| 2 | idx_sca_taskrecordentry |  | fid,fsubstarttime |

---

## 任务记录-主表 t_sca_taskrecord

- **表名称：** 任务记录-主表
- **表名：** t_sca_taskrecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftime | 耗时（秒） | int8 | 64 |  | √ | 0 | 耗时（秒） |
| 3 | fstatus | 状态 | varchar | 30 |  | √ | ' ' | 状态,枚举: 1 :未执行 2 :执行中 3 :失败 4 :成功 5 :警告 |
| 4 | fnextpagepara | 子页面参数 | varchar | 1000 |  | √ | ' ' | 子页面参数 |
| 5 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | ftaskconfigid | 配置ID | int8 | 64 |  | √ | 0 | 配置ID |
| 7 | fnextpagepara_tag | 子页面参数_详情 | text | 0 |  |  | null | 子页面参数_详情 |
| 8 | ftaskname | 任务名称 | varchar | 255 |  | √ | ' ' | 任务名称 |
| 9 | fprogress | 进度（%） | int8 | 64 |  | √ | 0 | 进度（%） |
| 10 | fstarttime | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 11 | fexecutorid | 执行人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fnextpage | 结束页面 | varchar | 50 |  | √ | ' ' | 结束页面 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_sca_taskrecord_pkey |  | fid |
| 2 | idx_sca_taskrecord |  | fstarttime,fexecutorid |
