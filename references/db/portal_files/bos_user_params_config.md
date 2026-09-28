# 个人参数设置-bos_user_params_config

## 个人参数设置-主表 t_bas_user_paras_config

- **表名称：** 个人参数设置-主表
- **表名：** t_bas_user_paras_config

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fusenewportal | 是否启用新门户 | bpchar | 1 |  |  | '0' | 是否启用新门户 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | ftablerowhigh | 行高 | int4 | 32 |  | √ | 32 | 行高 |
| 6 | fuserid | 用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | ftablevertical | 竖分割线 | bpchar | 1 |  | √ | '0' | 竖分割线 |
| 9 | freceivemessage | 是否接收运营类消息 | bpchar | 1 |  |  | '1' | 是否接收运营类消息 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | ftabledisplaymode | 显示模式 | varchar | 30 |  | √ | 'adaptive' | 显示模式,枚举: adaptive :居左 fit :等分 |
| 12 | ftableallenable | 全部开启 | bpchar | 1 |  | √ | '0' | 全部开启 |
| 13 | fappearancemode | 外观模式 | varchar | 50 |  | √ | ' ' | 外观模式 |
| 14 | ftableisgridstriped | 斑马纹 | bpchar | 1 |  | √ | '0' | 斑马纹 |
| 15 | ffirstnewportal | 是否首次使用新门户 | bpchar | 1 |  | √ | '0' | 是否首次使用新门户 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_user_paras_config_user |  | fuserid |
| 2 | pk_t_bas_user_paras_config |  | fid |
