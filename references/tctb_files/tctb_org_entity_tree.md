# 税务组织实体树（仅供查询展示组织树）-tctb_org_entity_tree

## 税务组织实体树（仅供查询展示组织树）-主表 t_tctb_org

- **表名称：** 税务组织实体树（仅供查询展示组织树）-主表
- **表名：** t_tctb_org

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | factivedate | factivedate | timestamp | 0 |  |  | null |  |
| 3 | fname | 组织名称 | varchar | 200 |  | √ | ' ' | 组织名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | forgfield | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fparentid | 上级组织id | int8 | 64 |  | √ | 0 | 税务组织实体树（仅供查询展示组织树） tctb_org_entity_tree |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fsourceid | 来源ID | varchar | 100 |  | √ | ' ' | 来源ID |
| 9 | flongnumber | 长编码 | varchar | 200 |  | √ | ' ' | 长编码 |
| 10 | fsourcesys | 来源系统 | varchar | 30 |  | √ | ' ' | 来源系统,枚举: 1 :苍穹 2 :EAS |
| 11 | factiveuserid | factiveuserid | int8 | 64 |  | √ | 0 |  |
| 12 | fparentname | 上级组织名称 | varchar | 200 |  | √ | ' ' | 上级组织名称 |
| 13 | fmodifytime | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 14 | fstatus | 组织状态 | varchar | 30 |  | √ | ' ' | 组织状态,枚举: 1 :保存 2 :启用 3 :禁用 |
| 15 | fcanceluserid | fcanceluserid | int8 | 64 |  | √ | 0 |  |
| 16 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | flicensestatus | flicensestatus | varchar | 30 |  | √ | 'A' |  |
| 18 | fcanceldate | fcanceldate | timestamp | 0 |  |  | null |  |
| 19 | fnumber | 组织编码 | varchar | 100 |  | √ | ' ' | 组织编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_tctb_org_fnumber |  | fnumber |
| 2 | t_tctb_org_pkey |  | fid |
