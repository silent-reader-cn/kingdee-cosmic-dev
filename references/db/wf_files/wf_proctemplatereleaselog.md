# 流程模板版本记录-wf_proctemplatereleaselog

## 流程模板版本记录-主表 t_wf_proctplreleaselog

- **表名称：** 流程模板版本记录-主表
- **表名：** t_wf_proctplreleaselog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreatedate | 操作时间 | timestamp | 0 |  |  | null | 操作时间 |
| 3 | fcreatorid | 操作人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fnewresourceid | 资源ID | int8 | 64 |  | √ | 0 | 资源ID |
| 5 | foldresourceid | 上一版本资源ID | int8 | 64 |  | √ | 0 | 上一版本资源ID |
| 6 | fproctplid | 流程模板 | int8 | 64 |  | √ | 0 | [流程模板 wf_proctemplate](../wf_files/wf_proctemplate.md) |
| 7 | fversion | 版本 | int4 | 32 |  | √ | 0 | 版本 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_wf_proctplreleaselog |  | fid |
| 2 | idx_wf_proctplreleaselog_tpl |  | fproctplid,fversion |
| 3 | idx_wf_proctplreleaselog_time |  | fcreatedate |
| 4 | idx_wf_proctplreleaselog_user |  | fcreatorid |
