# 调度任务-fcs_snapschedule

## 调度任务-主表 t_fcs_snapschedule

- **表名称：** 调度任务-主表
- **表名：** t_fcs_snapschedule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ffrequency | 快照版本 | varchar | 80 |  | √ | ' ' | 快照版本,枚举: realtime :查询频率 day :每天 |
| 3 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 4 | fmodifierid | 最后更新人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fcomment | fcomment | varchar | 255 |  | √ | ' ' |  |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fenabledate | 启用日期 | timestamp | 0 |  |  | null | 启用日期 |
| 8 | fdisabledate | 禁用日期 | timestamp | 0 |  |  | null | 禁用日期 |
| 9 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fqueryparam | 查询参数 | varchar | 255 |  | √ | ' ' | 查询参数 |
| 11 | fmodifytime | 最后更新时间 | timestamp | 0 |  |  | null | 最后更新时间 |
| 12 | fqueryitem | 查询方案 | varchar | 255 |  | √ | ' ' | 查询方案,枚举: |
| 13 | fqueryitem_tag | fqueryitem_tag | text | 0 |  |  | ' ' |  |
| 14 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 15 | fqueryparam_tag | 查询参数_详情 | text | 0 |  |  | ' ' | 查询参数_详情 |
| 16 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 18 | freporttype | 报表类型 | varchar | 30 |  | √ | ' ' | 报表类型,枚举: qing :轻分析报表 common :普通报表 |
| 19 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 20 | fenablerid | 启用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 21 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 22 | fformid | 报表 | varchar | 80 |  | √ | ' ' | 表单元数据 bos_formmeta |
| 23 | fqueryplugin | 数据取数插件 | varchar | 255 |  | √ | ' ' | 数据取数插件 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fcs_snapschedule |  | fid |
| 2 | idx_t_fcs_snapschedule |  | fnumber,fenable |

---

## 调度任务-多语言表 t_fcs_snapschedule_l

- **表名称：** 调度任务-多语言表
- **表名：** t_fcs_snapschedule_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 4 | flocaleid | flocaleid | varchar | 30 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fcs_snapschedule_l |  | fpkid |
| 2 | idx_t_fcs_snapschedule_l |  | fid,flocaleid |
