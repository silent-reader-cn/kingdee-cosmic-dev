# 转换任务-plm_plmdc_convert_task

## 转换任务-多语言表 t_plmdc_convert_task_l

- **表名称：** 转换任务-多语言表
- **表名：** t_plmdc_convert_task_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plmdc_convert_task_l_0 |  | fid,flocaleid |
| 2 | pk_t_plmdc_convert_task_l |  | fpkid |

---

## 转换任务-主表 t_plmdc_convert_task

- **表名称：** 转换任务-主表
- **表名：** t_plmdc_convert_task

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fexceptionmsg | 异常信息 | varchar | 255 |  | √ | ' ' | 异常信息 |
| 3 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | ftaskstate | 任务状态 | varchar | 30 |  | √ | ' ' | 任务状态,枚举: wait :待转换 switch :转换中 success :转换成功 fail :转换失败 |
| 6 | fbatchno | 批次号 | varchar | 50 |  | √ | ' ' | 批次号 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | ftasktype | 任务类型 | varchar | 50 |  | √ | ' ' | 任务类型 |
| 9 | fpriority | 优先级 | int4 | 32 |  | √ | 0 | 优先级 |
| 10 | ftaskdata_tag | 任务对象结构_详情 | text | 0 |  |  | null | 任务对象结构_详情 |
| 11 | ftaskdata | 任务对象结构 | varchar | 255 |  | √ | ' ' | 任务对象结构 |
| 12 | fswitchtype | 转换类型 | varchar | 30 |  | √ | ' ' | 转换类型,枚举: pdf :PDF light :轻量化 step :STEP html :HTML transfer :TRANSFER kingdee :KINGDEE iges :IGES |
| 13 | fstarttime | 闲时转换开始时间 | int4 | 32 |  | √ | '-1' | 闲时转换开始时间 |
| 14 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 15 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 16 | ftimeconsum | 转换耗时 | varchar | 50 |  | √ | ' ' | 转换耗时 |
| 17 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 19 | fretrytimes | 失败次数 | int4 | 32 |  | √ | 0 | 失败次数 |
| 20 | fsourcefile | 源文档 | int8 | 64 |  | √ | 0 | [物理文件属性 plm_plmdc_physical_file](../plmdc_files/plm_plmdc_physical_file.md) |
| 21 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 22 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 23 | fendtime | 闲时转换结束时间 | int4 | 32 |  | √ | '-1' | 闲时转换结束时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plmdc_converttask_source |  | fsourcefile |
| 2 | pk_t_plmdc_convert_task |  | fid |
