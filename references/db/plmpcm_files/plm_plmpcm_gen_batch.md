# 生成批次单据-plm_plmpcm_gen_batch

## 生成批次单据-主表 t_plmpcm_gen_batch

- **表名称：** 生成批次单据-主表
- **表名：** t_plmpcm_gen_batch

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgenbomid | 生成BOMID | int8 | 64 |  | √ | 0 | 生成BOMID |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fbomid | 配置BOMID | int8 | 64 |  | √ | 0 | 配置BOMID |
| 5 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fisverify | 是否是临时验证 | bpchar | 1 |  | √ | '0' | 是否是临时验证 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fiscompleted | 是否结束 | bpchar | 1 |  | √ | '0' | 是否结束 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid,fbomid,fisverify,fgenbomid,fcreatorid,fmodifierid |
| 2 | fbomid | fid,fbomid,fisverify,fgenbomid,fcreatorid,fmodifierid |
| 3 | fisverify | fid,fbomid,fisverify,fgenbomid,fcreatorid,fmodifierid |
| 4 | fgenbomid | fid,fbomid,fisverify,fgenbomid,fcreatorid,fmodifierid |
| 5 | fcreatorid | fid,fbomid,fisverify,fgenbomid,fcreatorid,fmodifierid |
| 6 | fmodifierid | fid,fbomid,fisverify,fgenbomid,fcreatorid,fmodifierid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plmpcm_gen_batch_fbomid |  | fbomid |
| 2 | pk_t_plmpcm_gen_batch |  | fid,fbomid,fisverify,fgenbomid,fcreatorid,fmodifierid |
| 3 | idx_plmpcm_gen_batch_fid |  | fid |
