# 生成结果及校验单据-plm_plmpcm_gen_result

## 生成结果及校验单据-主表 t_plmpcm_gen_result

- **表名称：** 生成结果及校验单据-主表
- **表名：** t_plmpcm_gen_result

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 生成对象名称 | varchar | 255 |  | √ | ' ' | 生成对象名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | frealvalue | 生成条件 | text | 0 |  |  | null | 生成条件 |
| 6 | fnewobj | 是否生成新对象 | bpchar | 1 |  | √ | '0' | 是否生成新对象 |
| 7 | foriginalitementryid | 原始BOM子项entryid | int8 | 64 |  | √ | 0 | 原始BOM子项entryid |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fmaterialsid | 生成物料 | int8 | 64 |  | √ | 0 | 生成物料 |
| 10 | fbomid | 生成BOM | int8 | 64 |  | √ | 0 | 生成BOM |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | foriginalmaterialid | 原始物料 | int8 | 64 |  | √ | 0 | 原始物料 |
| 13 | fbatchid | 计算批次id | int8 | 64 |  | √ | 0 | 计算批次id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid,fbomid,fbatchid,fcreatorid,fmodifierid |
| 2 | fbomid | fid,fbomid,fbatchid,fcreatorid,fmodifierid |
| 3 | fbatchid | fid,fbomid,fbatchid,fcreatorid,fmodifierid |
| 4 | fcreatorid | fid,fbomid,fbatchid,fcreatorid,fmodifierid |
| 5 | fmodifierid | fid,fbomid,fbatchid,fcreatorid,fmodifierid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plmpcm_gen_result_fbatchid |  | fbomid |
| 2 | pk_t_plmpcm_gen_result |  | fid,fbomid,fbatchid,fcreatorid,fmodifierid |
| 3 | idx_plmpcm_gen_result_fid |  | fid |
