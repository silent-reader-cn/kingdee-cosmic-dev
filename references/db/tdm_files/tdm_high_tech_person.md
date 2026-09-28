# 高新技术人员明细-tdm_high_tech_person

## 高新技术人员明细-主表 t_tdm_high_tech_person

- **表名称：** 高新技术人员明细-主表
- **表名：** t_tdm_high_tech_person

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fjobtitle | 职称 | varchar | 50 |  | √ | ' ' | 职称,枚举: A :高级职称 B :中级职称 C :初级职称 D :高级技工 E :无 |
| 3 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | fcreaterid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fentrytime | 入职时间 | timestamp | 0 |  |  | null | 入职时间 |
| 6 | fleavetime | 离职时间 | timestamp | 0 |  |  | null | 离职时间 |
| 7 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fuserid | 工号 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | feducation | 学历 | varchar | 50 |  | √ | ' ' | 学历,枚举: A :博士 B :硕士 C :本科 D :大专及以下 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fprofessional | 专业 | varchar | 255 |  | √ | ' ' | 专业 |
| 12 | fold | 年龄 | int8 | 64 |  | √ | 0 | 年龄 |
| 13 | fjob | 岗位 | varchar | 255 |  | √ | ' ' | 岗位 |
| 14 | fdatasource | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源,枚举: A :手工新增 B :模版引入 C :数据同步 |
| 15 | ftaxorgid | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tdm_hightp_org |  | ftaxorgid |
| 2 | pk_tdm_high_tech_person |  | fid |
