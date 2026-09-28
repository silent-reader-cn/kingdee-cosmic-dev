# 参数配置-chatbi_config

## 参数配置-主表 t_cbi_config

- **表名称：** 参数配置-主表
- **表名：** t_cbi_config

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fpicturevalue | 图片 | varchar | 255 |  | √ | ' ' | 图片 |
| 3 | fmodifierid | 最近更新人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcategory | 所属分类 | varchar | 50 |  | √ | ' ' | 所属分类,枚举: 0 :系统参数 1 :功能开关 2 :界面配置 3 :第三方对接参数 4 :其他 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | LOCALTIMESTAMP | 创建时间 |
| 6 | fencodevalue | 设值 | varchar | 2000 |  | √ | ' ' | 设值 |
| 7 | fsystem | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 8 | fmodifytime | 更新时间 | timestamp | 0 |  |  | LOCALTIMESTAMP | 更新时间 |
| 9 | fvalue | 使用值 | varchar | 2000 |  | √ | ' ' | 使用值 |
| 10 | ftype | 类型 | varchar | 50 |  | √ | ' ' | 类型,枚举: 1 :文本 2 :图片 3 :密文 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | ftextvalue | 设值 | varchar | 2000 |  | √ | ' ' | 设值 |
| 13 | fenable | 状态 | varchar | 50 |  | √ | ' ' | 状态,枚举: 1 :启用 0 :禁用 |
| 14 | fdesc | 说明 | varchar | 100 |  | √ | ' ' | 说明 |
| 15 | fcode | 编码 | varchar | 50 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cbi_config |  | fid |
