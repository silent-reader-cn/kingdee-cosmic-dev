# 用户首页功能关联表-mpdm_userfuncrelation

## 用户首页功能关联表-主表 t_mpdm_userfuncrel

- **表名称：** 用户首页功能关联表-主表
- **表名：** t_mpdm_userfuncrel

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ffuncsetid | 配置功能项 | int8 | 64 |  | √ | 0 | 移动首页功能 mpdm_functionconfig |
| 3 | fseqnumber | 顺序号 | int8 | 64 |  | √ | 0 | 顺序号 |
| 4 | fuserid | 用户 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpdm_userfuncrel |  | fid |
| 2 | idx_mpdm_userfuncrel_user |  | fuserid |
