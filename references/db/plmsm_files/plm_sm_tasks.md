# 查询下推日志-plm_sm_tasks

## 查询下推日志-主表 t_plmsm_tasks

- **表名称：** 查询下推日志-主表
- **表名：** t_plmsm_tasks

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fagentid | 代理任务id | int8 | 64 |  | √ | 0 | 代理任务id |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fparentid | 父任务id | int8 | 64 |  | √ | 0 | 父任务id |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | LOCALTIMESTAMP | 创建时间 |
| 6 | flayer | 层级 | int4 | 32 |  | √ | 0 | 层级 |
| 7 | fpushversionid | 下推版次 | int8 | 64 |  | √ | 0 | [BOM版次 plm_pdm_agg_bomview_v](../plmsm_files/plm_pdm_agg_bomview_v.md) |
| 8 | fparentbiz | 下推父BOM | int8 | 64 |  | √ | 0 | [BOM plm_pdm_agg_bomview](../plmsm_files/plm_pdm_agg_bomview.md) |
| 9 | fpushcost | 下推耗时 | varchar | 80 |  | √ | ' ' | 下推耗时 |
| 10 | fpushorgid | 下推组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 11 | fneedmessage | fneedmessage | int4 | 32 |  | √ | 0 |  |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | LOCALTIMESTAMP | 修改时间 |
| 13 | fstatus | 任务状态 | int4 | 32 |  | √ | 1 | 任务状态 |
| 14 | frootbiz | 下推根BOM | int8 | 64 |  | √ | 0 | [BOM plm_pdm_agg_bomview](../plmsm_files/plm_pdm_agg_bomview.md) |
| 15 | fstate | 下推状态 | varchar | 5 |  | √ | ' ' | 下推状态,枚举: 1 :失败 2 :正在执行 3 :成功 4 :失败 |
| 16 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fpushtype | 下推方式 | varchar | 50 |  | √ | ' ' | 下推方式,枚举: Add :新增 Update :更新 Delete :删除 Ecn :变更下推 |
| 18 | fpushbizid | 下推名称 | int8 | 64 |  | √ | 0 | [BOM plm_pdm_agg_bomview](../plmsm_files/plm_pdm_agg_bomview.md) |
| 19 | fbusinesstypeid | 下推分类 | int8 | 64 |  | √ | 0 | [PDM模型 plm_plmsm_modeltreedata](../plmsm_files/plm_plmsm_modeltreedata.md) |
| 20 | fnumber | 任务标志key | varchar | 100 |  | √ | ' ' | 任务标志key |
| 21 | fdesc | 任务描述 | varchar | 1024 |  | √ | ' ' | 任务描述 |
| 22 | ftaskid | 任务id | int8 | 64 |  | √ | 0 | 任务id |
| 23 | fsendmessage | 是否需要发送消息 | int4 | 32 |  | √ | 0 | 是否需要发送消息 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | index_plm_sm_tasks |  | fnumber,ftaskid |
| 2 | pk_t_plmsm_tasks |  | fid |
