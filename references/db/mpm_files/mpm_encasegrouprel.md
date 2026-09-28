# 项目装箱单组号关联关系-mpm_encasegrouprel

## 项目装箱单组号关联关系-主表 t_mpm_encgrouprel

- **表名称：** 项目装箱单组号关联关系-主表
- **表名：** t_mpm_encgrouprel

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcurseq | 本组序号 | int8 | 64 |  | √ | 0 | 本组序号 |
| 3 | fbillid | 装箱单id | int8 | 64 |  | √ | 0 | 装箱单id |
| 4 | fgroupnum | 组号 | int8 | 64 |  | √ | 0 | [组号 mpm_groupnumber](../mpm_files/mpm_groupnumber.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpm_encgrouprel_g |  | fgroupnum |
| 2 | pk_mpm_encgrouprel |  | fid |
| 3 | idx_mpm_encgrouprel_bid |  | fbillid |
