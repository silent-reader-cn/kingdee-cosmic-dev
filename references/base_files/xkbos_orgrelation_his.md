# 业务单元分配部门历史-xkbos_orgrelation_his

## 业务单元分配部门历史-主表 t_xkbos_orgrelation_his

- **表名称：** 业务单元分配部门历史-主表
- **表名：** t_xkbos_orgrelation_his

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | frelationid | 业务单元分配部门ID | int8 | 64 |  | √ | 0 | 业务单元分配部门ID |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fbizorgid | 业务单元 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fadminorgid | 行政组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_org_rela_his_ids |  | frelationid,fbizorgid,fadminorgid |
| 2 | pk_t_xkbos_orgrelation_his |  | fid |
